"""
Configuration for Everett RAG System
"""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent
MANUSCRIPTS_DIR = BASE_DIR / "transcribed_everett_manuscripts"
DATA_DIR = BASE_DIR / "data"
CHUNKS_DIR = DATA_DIR / "chunks"
INDEX_DIR = DATA_DIR / "index"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
CHUNKS_DIR.mkdir(exist_ok=True)
INDEX_DIR.mkdir(exist_ok=True)

# AWS Configuration
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Bedrock Model IDs
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"
LLM_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"  # Cheap & good

# Chunking Configuration
CHUNK_SIZE = 1000  # tokens
CHUNK_OVERLAP = 200  # tokens

# Retrieval Configuration
TOP_K_RESULTS = 5  # Number of chunks to retrieve

# Generation Configuration
MAX_TOKENS = 1024
TEMPERATURE = 0.7

# System prompt for the RAG
SYSTEM_PROMPT = """You are an expert assistant helping researchers and students explore Hugh Everett III's manuscripts and the development of the Many-Worlds Interpretation of quantum mechanics.

You have access to Everett's original handwritten drafts, thesis versions, correspondence with physicists like John Wheeler and Bryce DeWitt, and various notes from 1955-1957.

When answering questions:
1. Ground your responses in the actual manuscript content provided
2. Quote relevant passages when helpful
3. Cite the specific document sources (e.g., "In his handwritten draft from 1955...")
4. Explain the historical and scientific context when relevant
5. Be honest when information isn't available in the manuscripts

Help users understand how Everett developed his revolutionary ideas about quantum mechanics and the universal wave function."""

