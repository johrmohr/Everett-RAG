# Everett RAG System

A Retrieval-Augmented Generation (RAG) system for Hugh Everett III's manuscripts, built with completely free and open-source tools.

## Overview

This project provides a searchable interface for Hugh Everett III's scientific manuscripts, particularly his groundbreaking work on the Many-Worlds Interpretation of quantum mechanics. The system uses modern NLP techniques to enable semantic search and intelligent question-answering about Everett's work.

## Features

- **OCR Processing**: Convert scanned manuscripts to searchable text using Tesseract
- **Semantic Search**: Find relevant passages using vector embeddings
- **Local Vector Storage**: ChromaDB for efficient similarity search
- **Question Answering**: RAG-based responses using local LLMs
- **Web Interface**: Simple UI for searching and querying manuscripts
- **100% Free**: All components run locally with no API costs

## Technology Stack

- **Vector Database**: ChromaDB (local storage)
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **LLM**: Ollama with Llama2/Mistral (local execution)
- **OCR**: Tesseract
- **Backend**: Python, FastAPI, LangChain
- **Frontend**: HTML/CSS/JavaScript

## Installation

### Prerequisites

1. Python 3.12+
2. Tesseract OCR (`brew install tesseract` on macOS)
3. Ollama (optional, for LLM functionality)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/johrmohr/Everett-RAG.git
cd Everett-RAG
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Test installation:
```bash
python test_installation.py
```

## Usage

### Step 1: OCR Processing
Process manuscripts in the `Manuscripts/` folder:
```bash
python src/ocr.py
```

### Step 2: Build Vector Database
Create embeddings and populate ChromaDB:
```bash
python src/ingestion.py
```

### Step 3: Run the API
Start the FastAPI server:
```bash
uvicorn src.api:app --reload
```

### Step 4: Access the Interface
Open your browser to `http://localhost:8000`

## Project Structure

```
Everett-RAG/
├── Manuscripts/         # Source PDF/image files
├── processed_texts/     # OCR output
├── src/                 # Python source code
├── frontend/            # Web interface
├── chroma_db/           # Vector database storage
├── logs/                # Application logs
├── config.yaml          # Configuration
└── requirements.txt     # Python dependencies
```

## Configuration

Edit `config.yaml` to customize:
- Chunk sizes for document processing
- Embedding model selection
- LLM provider and model
- API settings

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Hugh Everett III for his revolutionary contributions to quantum mechanics
- The open-source community for providing free tools that make this project possible