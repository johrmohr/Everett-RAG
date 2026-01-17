"""
Complete RAG pipeline combining retrieval and generation
"""
from pathlib import Path
from typing import List, Dict, Any, Optional, Generator
from dataclasses import dataclass, field

import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import TOP_K_RESULTS
from src.rag.retriever import EverettRetriever, format_context
from src.rag.generator import EverettGenerator


@dataclass
class ChatMessage:
    """A message in the conversation"""
    role: str  # "user" or "assistant"
    content: str
    sources: Optional[List[Dict[str, Any]]] = None


@dataclass
class ChatSession:
    """Maintains conversation state"""
    messages: List[ChatMessage] = field(default_factory=list)
    
    def add_message(self, role: str, content: str, sources: Optional[List[Dict[str, Any]]] = None):
        self.messages.append(ChatMessage(role=role, content=content, sources=sources))
    
    def get_history_for_llm(self, max_messages: int = 10) -> List[Dict[str, str]]:
        """Get conversation history in LLM format"""
        # Get recent messages, excluding the last user message (that's the current query)
        recent = self.messages[-(max_messages + 1):-1] if len(self.messages) > 1 else []
        
        return [
            {"role": msg.role, "content": msg.content}
            for msg in recent
        ]
    
    def clear(self):
        self.messages = []


class EverettRAG:
    """
    Complete RAG system for the Everett manuscripts.
    Combines retrieval and generation with conversation management.
    """
    
    def __init__(self):
        """Initialize the RAG components"""
        self.retriever = EverettRetriever()
        self.generator = EverettGenerator()
        self.session = ChatSession()
        self._loaded = False
        
    def load(self) -> None:
        """Load all components"""
        if self._loaded:
            return
            
        print("Loading Everett RAG system...")
        self.retriever.load()
        self._loaded = True
        print("RAG system ready!")
        
    def query(
        self,
        question: str,
        include_sources: bool = True,
        min_similarity: float = 0.35,
        system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process a user query and generate a response.
        
        Uses dynamic threshold-based retrieval - only returns sources
        that are actually relevant to the query.
        
        Args:
            question: The user's question
            include_sources: Whether to include source information
            min_similarity: Minimum cosine similarity for a source to be included
            
        Returns:
            Dict with 'answer', 'sources', and other metadata
        """
        if not self._loaded:
            self.load()
        
        # Add user message to session
        self.session.add_message("user", question)
        
        # Retrieve relevant chunks using dynamic threshold
        # This automatically filters out irrelevant results
        results = self.retriever.search_with_threshold(
            question,
            min_similarity=min_similarity,
            candidate_pool=15,  # Fetch 15 candidates
            max_results=8       # Return at most 8
        )

        # If no results pass threshold, fall back to top-k with lower threshold
        if not results:
            results = self.retriever.search_with_threshold(
                question,
                min_similarity=0.20,  # Lower threshold
                candidate_pool=15,
                max_results=5
            )

        # Format context for the LLM
        context = format_context(results)
        
        # Get conversation history
        history = self.session.get_history_for_llm()
        
        # Generate response
        answer = self.generator.generate(
            query=question,
            context=context,
            conversation_history=history,
            system_prompt=system_prompt
        )
        
        # Extract source information
        sources = []
        if include_sources:
            for chunk, score in results:
                title = chunk.metadata.get("title", "Unknown")
                # Get filename from metadata, or construct from title
                filename = chunk.metadata.get("filename", "")
                if not filename and title != "Unknown":
                    filename = title + ".md"
                sources.append({
                    "title": title,
                    "doc_type": chunk.metadata.get("doc_type", "unknown"),
                    "year": chunk.metadata.get("year", "unknown"),
                    "relevance": round(score, 3),
                    "excerpt": chunk.content[:300] + "..." if len(chunk.content) > 300 else chunk.content,
                    "filename": filename
                })
        
        # Add assistant response to session
        self.session.add_message("assistant", answer, sources)
        
        return {
            "answer": answer,
            "sources": sources,
            "query": question,
            "chunks_retrieved": len(results)
        }
    
    def query_streaming(
        self,
        question: str,
        min_similarity: float = 0.35
    ) -> Generator[str, None, Dict[str, Any]]:
        """
        Process a query with streaming response.
        
        Yields:
            Chunks of the response text
            
        Returns:
            Final result dict with sources
        """
        if not self._loaded:
            self.load()
        
        # Add user message to session
        self.session.add_message("user", question)
        
        # Retrieve relevant chunks with dynamic threshold
        results = self.retriever.search_with_threshold(
            question,
            min_similarity=min_similarity,
            candidate_pool=15,
            max_results=8
        )

        # If no results pass threshold, fall back to lower threshold
        if not results:
            results = self.retriever.search_with_threshold(
                question,
                min_similarity=0.20,
                candidate_pool=15,
                max_results=5
            )

        context = format_context(results)
        history = self.session.get_history_for_llm()
        
        # Stream the response
        full_response = ""
        for chunk in self.generator.generate_streaming(
            query=question,
            context=context,
            conversation_history=history
        ):
            full_response += chunk
            yield chunk
        
        # Extract sources
        sources = []
        for chunk, score in results:
            title = chunk.metadata.get("title", "Unknown")
            # Get filename from metadata, or construct from title
            filename = chunk.metadata.get("filename", "")
            if not filename and title != "Unknown":
                filename = title + ".md"
            sources.append({
                "title": title,
                "doc_type": chunk.metadata.get("doc_type", "unknown"),
                "year": chunk.metadata.get("year", "unknown"),
                "relevance": round(score, 3),
                "excerpt": chunk.content[:300] + "...",
                "filename": filename
            })
        
        # Add to session
        self.session.add_message("assistant", full_response, sources)
        
        return {
            "answer": full_response,
            "sources": sources,
            "query": question
        }
    
    def clear_conversation(self) -> None:
        """Clear the conversation history"""
        self.session.clear()
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the full conversation history"""
        return [
            {
                "role": msg.role,
                "content": msg.content,
                "sources": msg.sources
            }
            for msg in self.session.messages
        ]


# Singleton instance for the API
_rag_instance: Optional[EverettRAG] = None

def get_rag() -> EverettRAG:
    """Get or create the RAG singleton"""
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = EverettRAG()
    return _rag_instance


if __name__ == "__main__":
    # Test the complete pipeline
    rag = EverettRAG()
    rag.load()
    
    # First question
    result = rag.query("What was Everett's main insight about quantum measurement?")
    print("Question:", result["query"])
    print("\nAnswer:", result["answer"])
    print("\nSources:")
    for source in result["sources"]:
        print(f"  - {source['title']} ({source['year']})")
    
    # Follow-up question
    print("\n" + "="*50 + "\n")
    result = rag.query("How did Wheeler respond to these ideas?")
    print("Question:", result["query"])
    print("\nAnswer:", result["answer"])

