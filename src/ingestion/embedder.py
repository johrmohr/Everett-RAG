"""
Embedding generation using AWS Bedrock Titan
"""
import json
import pickle
from pathlib import Path
from typing import List, Optional
import numpy as np
from tqdm import tqdm

import boto3
from botocore.config import Config

from .chunker import Chunk, load_chunks, save_chunks
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import AWS_REGION, EMBEDDING_MODEL_ID, INDEX_DIR, CHUNKS_DIR


class EverettEmbedder:
    """Handles embedding generation using AWS Bedrock Titan"""
    
    def __init__(self, region: str = AWS_REGION):
        """Initialize the Bedrock client"""
        config = Config(
            region_name=region,
            retries={"max_attempts": 3, "mode": "adaptive"}
        )
        
        self.client = boto3.client(
            service_name="bedrock-runtime",
            config=config
        )
        self.model_id = EMBEDDING_MODEL_ID
        self.embedding_dim = 1024  # Titan v2 dimension
        
    def embed_text(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.
        
        Args:
            text: The text to embed
            
        Returns:
            List of floats representing the embedding vector
        """
        # Titan has a 8192 token limit, truncate if needed
        if len(text) > 30000:  # Rough character limit
            text = text[:30000]
        
        body = json.dumps({
            "inputText": text,
            "dimensions": self.embedding_dim,
            "normalize": True
        })
        
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=body,
            contentType="application/json",
            accept="application/json"
        )
        
        response_body = json.loads(response["body"].read())
        return response_body["embedding"]
    
    def embed_texts(self, texts: List[str], batch_size: int = 10) -> np.ndarray:
        """
        Generate embeddings for multiple texts.
        
        Args:
            texts: List of texts to embed
            batch_size: Not used for Bedrock (no batch API), kept for interface compatibility
            
        Returns:
            NumPy array of shape (n_texts, embedding_dim)
        """
        embeddings = []
        
        for text in tqdm(texts, desc="Generating embeddings"):
            try:
                embedding = self.embed_text(text)
                embeddings.append(embedding)
            except Exception as e:
                print(f"Error embedding text: {e}")
                # Use zero vector as fallback
                embeddings.append([0.0] * self.embedding_dim)
        
        return np.array(embeddings, dtype=np.float32)
    
    def embed_chunks(self, chunks: List[Chunk]) -> np.ndarray:
        """
        Generate embeddings for a list of chunks.
        
        Args:
            chunks: List of Chunk objects
            
        Returns:
            NumPy array of embeddings
        """
        texts = [chunk.content for chunk in chunks]
        return self.embed_texts(texts)


def build_embeddings(
    chunks_path: Path = CHUNKS_DIR / "chunks.json",
    output_path: Path = INDEX_DIR / "embeddings.npy"
) -> np.ndarray:
    """
    Load chunks and generate embeddings for all of them.
    
    Args:
        chunks_path: Path to the chunks JSON file
        output_path: Path to save the embeddings
        
    Returns:
        NumPy array of embeddings
    """
    # Load chunks
    chunks = load_chunks(chunks_path)
    
    # Initialize embedder
    embedder = EverettEmbedder()
    
    # Generate embeddings
    print(f"Generating embeddings for {len(chunks)} chunks...")
    embeddings = embedder.embed_chunks(chunks)
    
    # Save embeddings
    np.save(output_path, embeddings)
    print(f"Saved embeddings to {output_path}")
    
    return embeddings


def load_embeddings(path: Path = INDEX_DIR / "embeddings.npy") -> np.ndarray:
    """Load embeddings from disk"""
    return np.load(path)


if __name__ == "__main__":
    embeddings = build_embeddings()
    print(f"Embeddings shape: {embeddings.shape}")

