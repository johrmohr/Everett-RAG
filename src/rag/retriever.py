"""
Vector retrieval using FAISS
"""
import json
import pickle
from pathlib import Path
from typing import List, Tuple, Optional
import numpy as np

import faiss

import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import INDEX_DIR, CHUNKS_DIR, TOP_K_RESULTS
from src.ingestion.chunker import Chunk, load_chunks
from src.ingestion.embedder import EverettEmbedder, load_embeddings


class EverettRetriever:
    """Handles vector similarity search for manuscript chunks"""
    
    def __init__(
        self,
        chunks_path: Path = CHUNKS_DIR / "chunks.json",
        index_path: Path = INDEX_DIR / "faiss.index",
        embeddings_path: Path = INDEX_DIR / "embeddings.npy"
    ):
        """
        Initialize the retriever.
        
        Args:
            chunks_path: Path to the chunks JSON file
            index_path: Path to the FAISS index
            embeddings_path: Path to the embeddings numpy file
        """
        self.chunks_path = chunks_path
        self.index_path = index_path
        self.embeddings_path = embeddings_path
        
        self.chunks: List[Chunk] = []
        self.index: Optional[faiss.Index] = None
        self.embedder: Optional[EverettEmbedder] = None
        
    def load(self) -> None:
        """Load the chunks and FAISS index from disk"""
        # Load chunks
        self.chunks = load_chunks(self.chunks_path)
        
        # Load or build FAISS index
        if self.index_path.exists():
            print(f"Loading FAISS index from {self.index_path}")
            self.index = faiss.read_index(str(self.index_path))
        else:
            print("FAISS index not found, building...")
            self.build_index()
        
        # Initialize embedder for query embedding
        self.embedder = EverettEmbedder()
        
        print(f"Retriever loaded with {len(self.chunks)} chunks")
        
    def build_index(self) -> None:
        """Build the FAISS index from embeddings"""
        # Load embeddings
        embeddings = load_embeddings(self.embeddings_path)
        
        # Create FAISS index
        # Using IndexFlatIP for inner product (cosine similarity with normalized vectors)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)
        
        # Add to index
        self.index.add(embeddings)
        
        # Save index
        faiss.write_index(self.index, str(self.index_path))
        print(f"Built and saved FAISS index with {self.index.ntotal} vectors")
        
    def search(
        self,
        query: str,
        top_k: int = TOP_K_RESULTS
    ) -> List[Tuple[Chunk, float]]:
        """
        Search for relevant chunks given a query.
        
        Args:
            query: The search query
            top_k: Number of results to return
            
        Returns:
            List of (Chunk, score) tuples, sorted by relevance
        """
        if self.index is None or self.embedder is None:
            raise RuntimeError("Retriever not loaded. Call load() first.")
        
        # Embed the query
        query_embedding = np.array([self.embedder.embed_text(query)], dtype=np.float32)
        
        # Normalize for cosine similarity
        faiss.normalize_L2(query_embedding)
        
        # Search
        scores, indices = self.index.search(query_embedding, top_k)
        
        # Build results
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < len(self.chunks):
                results.append((self.chunks[idx], float(score)))
        
        return results
    
    def search_with_threshold(
        self,
        query: str,
        min_similarity: float = 0.35,
        candidate_pool: int = 10,
        max_results: int = 8
    ) -> List[Tuple[Chunk, float]]:
        """
        Search with dynamic similarity threshold.
        
        Uses cosine similarity (IndexFlatIP with normalized vectors).
        Higher scores = better matches (range: 0.0 to 1.0).
        
        Args:
            query: The search query
            min_similarity: Minimum cosine similarity threshold (0.0 to 1.0)
                           Only results with similarity >= this are returned.
                           Default 0.35 works well for this corpus.
            candidate_pool: Number of candidates to fetch from FAISS
            max_results: Maximum number of results to return
            
        Returns:
            List of (Chunk, score) tuples that pass the threshold,
            sorted by relevance. Empty list if none pass.
        """
        if self.index is None or self.embedder is None:
            raise RuntimeError("Retriever not loaded. Call load() first.")
        
        # Embed the query
        query_embedding = np.array([self.embedder.embed_text(query)], dtype=np.float32)
        
        # Normalize for cosine similarity
        faiss.normalize_L2(query_embedding)
        
        # Search for candidate pool
        scores, indices = self.index.search(query_embedding, candidate_pool)
        
        # Filter by threshold
        results = []
        for score, idx in zip(scores[0], indices[0]):
            # Skip invalid indices
            if idx < 0 or idx >= len(self.chunks):
                continue
            
            # Only keep results above the similarity threshold
            if score >= min_similarity:
                results.append((self.chunks[idx], float(score)))
        
        # Cap at max_results
        return results[:max_results]
    
    def search_with_filter(
        self,
        query: str,
        top_k: int = TOP_K_RESULTS,
        doc_type: Optional[str] = None,
        year: Optional[str] = None
    ) -> List[Tuple[Chunk, float]]:
        """
        Search with metadata filtering.
        
        Args:
            query: The search query
            top_k: Number of results to return
            doc_type: Filter by document type
            year: Filter by year
            
        Returns:
            Filtered list of (Chunk, score) tuples
        """
        # Get more results than needed for filtering
        results = self.search(query, top_k=top_k * 3)
        
        # Apply filters
        filtered = []
        for chunk, score in results:
            if doc_type and chunk.metadata.get("doc_type") != doc_type:
                continue
            if year and chunk.metadata.get("year") != year:
                continue
            filtered.append((chunk, score))
            
            if len(filtered) >= top_k:
                break
        
        return filtered


def format_context(results: List[Tuple[Chunk, float]]) -> str:
    """
    Format retrieved chunks into a context string for the LLM.
    
    Args:
        results: List of (Chunk, score) tuples
        
    Returns:
        Formatted context string
    """
    context_parts = []
    
    for i, (chunk, score) in enumerate(results, 1):
        meta = chunk.metadata
        source = meta.get("title", "Unknown")
        doc_type = meta.get("doc_type", "document")
        year = meta.get("year", "unknown year")
        
        context_parts.append(f"""
---
**Source {i}:** {source}
**Type:** {doc_type} | **Year:** {year} | **Relevance:** {score:.3f}

{chunk.content}
""")
    
    return "\n".join(context_parts)


if __name__ == "__main__":
    # Test the retriever
    retriever = EverettRetriever()
    retriever.load()
    
    query = "How did Everett explain the measurement problem?"
    results = retriever.search(query)
    
    print(f"\nQuery: {query}")
    print(f"Found {len(results)} results:\n")
    
    for chunk, score in results:
        print(f"Score: {score:.3f}")
        print(f"Source: {chunk.metadata['title']}")
        print(f"Content: {chunk.content[:200]}...")
        print()

