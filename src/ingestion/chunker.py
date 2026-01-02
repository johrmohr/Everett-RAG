"""
Smart text chunking for Everett manuscripts
"""
import re
from typing import List, Dict, Any
from dataclasses import dataclass
import json
from pathlib import Path
from tqdm import tqdm

from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken

from .loader import Document


@dataclass  
class Chunk:
    """Represents a chunk of text with metadata"""
    id: str
    content: str
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "content": self.content,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Chunk":
        return cls(
            id=data["id"],
            content=data["content"],
            metadata=data["metadata"]
        )


def count_tokens(text: str, model: str = "cl100k_base") -> int:
    """Count tokens in text using tiktoken"""
    try:
        encoding = tiktoken.get_encoding(model)
        return len(encoding.encode(text))
    except Exception:
        # Fallback: rough estimate
        return len(text) // 4


def create_chunk_id(doc_title: str, chunk_index: int) -> str:
    """Create a unique chunk ID"""
    # Clean title for ID
    clean_title = re.sub(r'[^a-zA-Z0-9]', '_', doc_title)[:50]
    return f"{clean_title}_{chunk_index:04d}"


def chunk_documents(
    documents: List[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Chunk]:
    """
    Chunk documents using recursive character splitting.
    
    Args:
        documents: List of Document objects
        chunk_size: Target chunk size in characters
        chunk_overlap: Overlap between chunks in characters
        
    Returns:
        List of Chunk objects
    """
    # Initialize the text splitter
    # Use markdown-aware separators for better chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=[
            "\n## ",      # Major headers
            "\n### ",     # Minor headers
            "\n\n",       # Paragraphs
            "\n",         # Lines
            ". ",         # Sentences
            " ",          # Words
            ""            # Characters
        ]
    )
    
    all_chunks = []
    
    print(f"Chunking {len(documents)} documents...")
    
    for doc in tqdm(documents, desc="Chunking documents"):
        # Split the document
        text_chunks = splitter.split_text(doc.content)
        
        for i, chunk_text in enumerate(text_chunks):
            # Skip very small chunks
            if len(chunk_text.strip()) < 50:
                continue
            
            chunk_id = create_chunk_id(doc.metadata["title"], i)
            
            # Create chunk metadata (inherit from document)
            chunk_metadata = doc.metadata.copy()
            chunk_metadata["chunk_index"] = i
            chunk_metadata["total_chunks"] = len(text_chunks)
            chunk_metadata["token_count"] = count_tokens(chunk_text)
            
            all_chunks.append(Chunk(
                id=chunk_id,
                content=chunk_text,
                metadata=chunk_metadata
            ))
    
    print(f"Created {len(all_chunks)} chunks from {len(documents)} documents")
    
    # Print statistics
    token_counts = [c.metadata["token_count"] for c in all_chunks]
    print(f"Token count stats: min={min(token_counts)}, max={max(token_counts)}, avg={sum(token_counts)//len(token_counts)}")
    
    return all_chunks


def save_chunks(chunks: List[Chunk], output_path: Path) -> None:
    """Save chunks to a JSON file"""
    data = [chunk.to_dict() for chunk in chunks]
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(chunks)} chunks to {output_path}")


def load_chunks(input_path: Path) -> List[Chunk]:
    """Load chunks from a JSON file"""
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    chunks = [Chunk.from_dict(item) for item in data]
    print(f"Loaded {len(chunks)} chunks from {input_path}")
    
    return chunks


if __name__ == "__main__":
    from config import MANUSCRIPTS_DIR, CHUNKS_DIR
    from .loader import load_manuscripts
    
    docs = load_manuscripts(MANUSCRIPTS_DIR)
    chunks = chunk_documents(docs)
    save_chunks(chunks, CHUNKS_DIR / "chunks.json")

