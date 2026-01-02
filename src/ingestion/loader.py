"""
Document loader for Everett manuscripts
"""
import re
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass
from tqdm import tqdm


@dataclass
class Document:
    """Represents a loaded manuscript document"""
    content: str
    metadata: Dict[str, Any]
    
    def __repr__(self):
        return f"Document(title='{self.metadata.get('title', 'Unknown')[:50]}...', chars={len(self.content)})"


def extract_metadata(filename: str) -> Dict[str, Any]:
    """
    Extract metadata from filename.
    
    Examples:
    - "Everett Handwritten Draft -- I Introduction circa 1955.md"
    - "Wheeler to Everett 21-May-1956.md"
    - "Everett long thesis as published 1973.md"
    """
    metadata = {
        "filename": filename,
        "title": filename.replace(".md", "").replace(".pdf", ""),
    }
    
    # Extract year
    year_match = re.search(r'(\d{4})', filename)
    if year_match:
        metadata["year"] = year_match.group(1)
    
    # Extract date if present (format: DD-Month-YYYY)
    date_match = re.search(r'(\d{1,2}-\w+-\d{4})', filename)
    if date_match:
        metadata["date"] = date_match.group(1)
    
    # Determine document type
    filename_lower = filename.lower()
    if "handwritten" in filename_lower:
        metadata["doc_type"] = "handwritten_draft"
    elif "draft" in filename_lower:
        metadata["doc_type"] = "typed_draft"
    elif "thesis" in filename_lower:
        metadata["doc_type"] = "thesis"
    elif " to " in filename_lower:
        metadata["doc_type"] = "correspondence"
        # Extract sender and recipient
        match = re.match(r'^(.+?) to (.+?) ', filename)
        if match:
            metadata["sender"] = match.group(1)
            metadata["recipient"] = match.group(2)
    elif "notes" in filename_lower or "fragment" in filename_lower:
        metadata["doc_type"] = "notes"
    elif "minipaper" in filename_lower:
        metadata["doc_type"] = "minipaper"
    else:
        metadata["doc_type"] = "other"
    
    # Check if it's an Everett document
    metadata["is_everett_author"] = filename.lower().startswith("everett")
    
    return metadata


def clean_content(content: str) -> str:
    """Clean and normalize markdown content"""
    # Remove excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove page break indicators
    content = re.sub(r'^---+$', '', content, flags=re.MULTILINE)
    
    # Clean up OCR artifacts like "Input" markers
    content = re.sub(r'^Input\s*$', '', content, flags=re.MULTILINE)
    
    # Remove excessive spaces
    content = re.sub(r'  +', ' ', content)
    
    return content.strip()


def load_manuscripts(manuscripts_dir: Path) -> List[Document]:
    """
    Load all manuscript markdown files from the directory.
    
    Args:
        manuscripts_dir: Path to the transcribed_everett_manuscripts folder
        
    Returns:
        List of Document objects with content and metadata
    """
    documents = []
    md_files = sorted(manuscripts_dir.glob("*.md"))
    
    print(f"Loading {len(md_files)} manuscript files...")
    
    for filepath in tqdm(md_files, desc="Loading manuscripts"):
        try:
            content = filepath.read_text(encoding="utf-8")
            content = clean_content(content)
            
            metadata = extract_metadata(filepath.name)
            metadata["filepath"] = str(filepath)
            metadata["char_count"] = len(content)
            
            documents.append(Document(content=content, metadata=metadata))
            
        except Exception as e:
            print(f"Error loading {filepath.name}: {e}")
    
    print(f"Successfully loaded {len(documents)} documents")
    
    # Print summary statistics
    doc_types = {}
    for doc in documents:
        doc_type = doc.metadata.get("doc_type", "unknown")
        doc_types[doc_type] = doc_types.get(doc_type, 0) + 1
    
    print("\nDocument types:")
    for doc_type, count in sorted(doc_types.items()):
        print(f"  {doc_type}: {count}")
    
    return documents


if __name__ == "__main__":
    from config import MANUSCRIPTS_DIR
    docs = load_manuscripts(MANUSCRIPTS_DIR)
    print(f"\nSample document: {docs[0]}")

