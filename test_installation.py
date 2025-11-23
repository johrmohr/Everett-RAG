#!/usr/bin/env python3
"""Test script to verify all dependencies are installed correctly."""

import sys
print("Testing Everett RAG System Dependencies...")
print("-" * 50)

def test_import(module_name, display_name=None):
    """Test if a module can be imported."""
    if display_name is None:
        display_name = module_name

    try:
        __import__(module_name)
        print(f"✓ {display_name} - OK")
        return True
    except ImportError as e:
        print(f"✗ {display_name} - FAILED: {e}")
        return False

# Test all major dependencies
all_passed = True

# Core dependencies
all_passed &= test_import("chromadb", "ChromaDB")
all_passed &= test_import("langchain", "LangChain")
all_passed &= test_import("langchain_community", "LangChain Community")
all_passed &= test_import("sentence_transformers", "Sentence Transformers")
all_passed &= test_import("fastapi", "FastAPI")
all_passed &= test_import("uvicorn", "Uvicorn")

# OCR dependencies
all_passed &= test_import("pytesseract", "PyTesseract (OCR)")
all_passed &= test_import("pdf2image", "PDF2Image")
all_passed &= test_import("PIL", "Pillow (Image Processing)")

# Document processing
all_passed &= test_import("pypdf", "PyPDF")
all_passed &= test_import("yaml", "PyYAML")
all_passed &= test_import("tqdm", "TQDM (Progress Bars)")
all_passed &= test_import("numpy", "NumPy")

# LLM
all_passed &= test_import("ollama", "Ollama (LLM)")

print("-" * 50)

# Check for Tesseract OCR installation
import subprocess
try:
    result = subprocess.run(['tesseract', '--version'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ Tesseract OCR - OK")
        print(f"  Version: {result.stdout.split()[1] if result.stdout.split() else 'Unknown'}")
    else:
        print("✗ Tesseract OCR - NOT FOUND")
        print("  Please install Tesseract: brew install tesseract")
        all_passed = False
except FileNotFoundError:
    print("✗ Tesseract OCR - NOT FOUND")
    print("  Please install Tesseract: brew install tesseract")
    all_passed = False

print("-" * 50)

# Test ChromaDB initialization
try:
    import chromadb
    client = chromadb.PersistentClient(path="./test_chroma")
    print("✓ ChromaDB initialization - OK")

    # Clean up test directory
    import shutil
    shutil.rmtree("./test_chroma", ignore_errors=True)
except Exception as e:
    print(f"✗ ChromaDB initialization - FAILED: {e}")
    all_passed = False

# Test embedding model download
try:
    from sentence_transformers import SentenceTransformer
    print("✓ Sentence Transformers import - OK")
    print("  Note: Embedding model will be downloaded on first use")
except Exception as e:
    print(f"✗ Sentence Transformers - FAILED: {e}")
    all_passed = False

print("-" * 50)
if all_passed:
    print("✅ All dependencies installed successfully!")
else:
    print("❌ Some dependencies are missing. Please check above for details.")
    sys.exit(1)