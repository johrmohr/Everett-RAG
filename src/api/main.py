"""
FastAPI backend for Everett RAG system
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.rag.pipeline import get_rag, EverettRAG

# Initialize FastAPI app
app = FastAPI(
    title="Everett Manuscripts RAG API",
    description="Explore Hugh Everett III's manuscripts on the Many-Worlds Interpretation",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    include_sources: bool = True
    
class Source(BaseModel):
    title: str
    doc_type: str
    year: str
    relevance: float
    excerpt: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
    query: str
    chunks_retrieved: int

class ConversationMessage(BaseModel):
    role: str
    content: str
    sources: Optional[List[Source]] = None

class HealthResponse(BaseModel):
    status: str
    loaded: bool
    chunks_count: int


# Global RAG instance
rag: Optional[EverettRAG] = None


@app.on_event("startup")
async def startup_event():
    """Load the RAG system on startup"""
    global rag
    try:
        rag = get_rag()
        rag.load()
        print("RAG system loaded successfully!")
    except Exception as e:
        print(f"Warning: Could not load RAG system: {e}")
        print("The system will attempt to load on first request.")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check if the system is ready"""
    global rag
    if rag is None:
        return HealthResponse(status="not_loaded", loaded=False, chunks_count=0)
    
    try:
        chunks_count = len(rag.retriever.chunks) if rag._loaded else 0
        return HealthResponse(
            status="healthy",
            loaded=rag._loaded,
            chunks_count=chunks_count
        )
    except Exception as e:
        return HealthResponse(status=f"error: {str(e)}", loaded=False, chunks_count=0)


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message and get a response with sources.
    Uses dynamic threshold-based retrieval - automatically returns
    only sources that are actually relevant to the query.
    """
    global rag
    
    if rag is None:
        rag = get_rag()
    
    try:
        if not rag._loaded:
            rag.load()
        
        result = rag.query(
            question=request.message,
            include_sources=request.include_sources
        )
        
        return ChatResponse(
            answer=result["answer"],
            sources=[Source(**s) for s in result["sources"]],
            query=result["query"],
            chunks_retrieved=result["chunks_retrieved"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """
    Send a message and get a streaming response.
    Uses dynamic threshold-based retrieval.
    """
    global rag
    
    if rag is None:
        rag = get_rag()
    
    if not rag._loaded:
        rag.load()
    
    async def generate():
        try:
            # Get results using dynamic threshold
            results = rag.retriever.search_with_threshold(
                request.message,
                min_similarity=0.35,
                candidate_pool=15,
                max_results=8
            )
            
            # Build sources
            sources = []
            for chunk, score in results:
                sources.append({
                    "title": chunk.metadata.get("title", "Unknown"),
                    "doc_type": chunk.metadata.get("doc_type", "unknown"),
                    "year": chunk.metadata.get("year", "unknown"),
                    "relevance": round(score, 3),
                    "excerpt": chunk.content[:300] + "..."
                })
            
            # Stream the response
            from src.rag.retriever import format_context
            context = format_context(results)
            history = rag.session.get_history_for_llm()
            
            full_response = ""
            for chunk in rag.generator.generate_streaming(
                query=request.message,
                context=context,
                conversation_history=history
            ):
                full_response += chunk
                yield f"data: {json.dumps({'type': 'token', 'content': chunk})}\n\n"
            
            # Send sources at the end
            yield f"data: {json.dumps({'type': 'sources', 'sources': sources})}\n\n"
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
            
            # Update session
            rag.session.add_message("user", request.message)
            rag.session.add_message("assistant", full_response, sources)
            
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )


@app.get("/conversation", response_model=List[ConversationMessage])
async def get_conversation():
    """Get the current conversation history"""
    global rag
    
    if rag is None or not rag._loaded:
        return []
    
    history = rag.get_conversation_history()
    return [ConversationMessage(**msg) for msg in history]


@app.post("/conversation/clear")
async def clear_conversation():
    """Clear the conversation history"""
    global rag
    
    if rag is not None:
        rag.clear_conversation()
    
    return {"status": "cleared"}


@app.get("/")
async def root():
    """Serve the frontend"""
    static_path = Path(__file__).parent.parent.parent / "static" / "index.html"
    if static_path.exists():
        return FileResponse(static_path)
    return {"message": "Frontend not found. API is running at /api"}


@app.get("/api")
async def api_info():
    """API info endpoint"""
    return {
        "name": "Everett Manuscripts RAG API",
        "description": "Explore Hugh Everett III's manuscripts on the Many-Worlds Interpretation",
        "endpoints": {
            "/chat": "POST - Send a message and get a response",
            "/chat/stream": "POST - Send a message and get a streaming response",
            "/conversation": "GET - Get conversation history",
            "/conversation/clear": "POST - Clear conversation",
            "/documents": "GET - List all manuscripts",
            "/documents/{filename}": "GET - Get manuscript content",
            "/health": "GET - Health check"
        }
    }


import re

def parse_doc_metadata(filename: str) -> Dict[str, str]:
    """Extract metadata from filename"""
    title = filename.replace(".md", "").replace("_", " ")

    # Detect document type
    doc_type = "Other"
    if "Handwritten" in filename:
        doc_type = "Handwritten"
    elif "Letter" in filename or " to " in filename:
        doc_type = "Letter"
    elif "Thesis" in filename or "thesis" in filename:
        doc_type = "Thesis"

    # Extract year
    year_match = re.search(r'(19\d{2})', filename)
    year = year_match.group(1) if year_match else "—"

    return {"title": title, "doc_type": doc_type, "year": year, "filename": filename}


@app.get("/documents")
async def list_documents():
    """List all available manuscripts"""
    manuscripts_dir = Path(__file__).parent.parent.parent / "transcribed_everett_manuscripts"

    if not manuscripts_dir.exists():
        raise HTTPException(status_code=404, detail="Manuscripts directory not found")

    documents = []
    for f in sorted(manuscripts_dir.glob("*.md")):
        documents.append(parse_doc_metadata(f.name))

    return documents


@app.get("/documents/{filename:path}")
async def get_document(filename: str):
    """Get the content of a specific manuscript"""
    manuscripts_dir = Path(__file__).parent.parent.parent / "transcribed_everett_manuscripts"
    file_path = manuscripts_dir / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document not found")

    content = file_path.read_text(encoding="utf-8")
    metadata = parse_doc_metadata(filename)

    return {"content": content, **metadata}


# Mount static files (must be after all routes)
static_dir = Path(__file__).parent.parent.parent / "static"
if static_dir.exists():
    app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

