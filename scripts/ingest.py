#!/usr/bin/env python3
"""
Ingestion script for Everett manuscripts
Loads documents, chunks them, generates embeddings, and builds the FAISS index
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config import MANUSCRIPTS_DIR, CHUNKS_DIR, INDEX_DIR
from src.ingestion.loader import load_manuscripts
from src.ingestion.chunker import chunk_documents, save_chunks
from src.ingestion.embedder import EverettEmbedder
import numpy as np
import faiss


def main():
    print("=" * 60)
    print("Everett Manuscripts Ingestion Pipeline")
    print("=" * 60)
    
    # Step 1: Load manuscripts
    print("\n📚 Step 1: Loading manuscripts...")
    documents = load_manuscripts(MANUSCRIPTS_DIR)
    
    if not documents:
        print("❌ No documents found! Check the manuscripts directory.")
        return
    
    # Step 2: Chunk documents
    print("\n✂️ Step 2: Chunking documents...")
    chunks = chunk_documents(
        documents,
        chunk_size=1000,
        chunk_overlap=200
    )
    
    # Save chunks
    chunks_path = CHUNKS_DIR / "chunks.json"
    save_chunks(chunks, chunks_path)
    
    # Step 3: Generate embeddings
    print("\n🧮 Step 3: Generating embeddings with AWS Bedrock Titan...")
    print("   (This may take a few minutes and will use AWS credits)")
    
    embedder = EverettEmbedder()
    embeddings = embedder.embed_chunks(chunks)
    
    # Save embeddings
    embeddings_path = INDEX_DIR / "embeddings.npy"
    np.save(embeddings_path, embeddings)
    print(f"   Saved embeddings to {embeddings_path}")
    print(f"   Embeddings shape: {embeddings.shape}")
    
    # Step 4: Build FAISS index
    print("\n🔍 Step 4: Building FAISS index...")
    
    # Normalize for cosine similarity
    faiss.normalize_L2(embeddings)
    
    # Create index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    
    # Save index
    index_path = INDEX_DIR / "faiss.index"
    faiss.write_index(index, str(index_path))
    print(f"   Saved FAISS index to {index_path}")
    print(f"   Index contains {index.ntotal} vectors")
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ Ingestion Complete!")
    print("=" * 60)
    print(f"""
Summary:
  - Documents loaded: {len(documents)}
  - Chunks created: {len(chunks)}
  - Embedding dimension: {dimension}
  - Index vectors: {index.ntotal}
  
Files created:
  - {chunks_path}
  - {embeddings_path}
  - {index_path}

Next steps:
  1. Start the API server: python -m src.api.main
  2. Start the frontend: streamlit run frontend/app.py
""")


if __name__ == "__main__":
    main()

