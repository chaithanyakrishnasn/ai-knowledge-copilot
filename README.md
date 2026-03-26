# AI Knowledge Copilot (RAG-based Enterprise Assistant)

An end-to-end AI system that enables intelligent document querying using Retrieval-Augmented Generation (RAG), semantic search, and conversational memory.

---

## Features

- FastAPI-based backend APIs  
- Retrieval-Augmented Generation (RAG) pipeline  
- SentenceTransformers embedding model  
- Chroma vector database for semantic search  
- OpenAI/GPT-based LLM for answer generation  
- Conversational memory for multi-turn chat  
- Logging, error handling, and production-ready architecture  

---

## Current Demo Capabilities

- Ingest and process PDF documents  
- Generate embeddings using a local model  
- Store embeddings in Chroma vector database  
- Answer queries using semantic retrieval + LLM  
- Provide source attribution for transparency  
- Maintain chat history for contextual conversations  

---

## Project Architecture

```
backend/        # FastAPI APIs (ingestion, query, chat memory)
src/
├── services/   # RAG pipeline (chunking, embeddings, LLM, memory)
├── db/         # Vector database integration (Chroma)
├── core/       # Config, logging, environment management

data/           # Uploaded documents (runtime)
logs/           # Application logs (runtime)
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-knowledge-copilot.git
cd ai-knowledge-copilot
```

---

### 2. Configure Environment

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
ENV=development
DEBUG=True
```

---

### 3. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

### 4. Run the Backend

```bash
uvicorn main:app --reload
```

---

### 5. Access the API

- API Docs:  
  `http://localhost:8000/docs`

- Health Check:  
  `http://localhost:8000/health`

---

## Upload Documents

Use the `/upload-doc` endpoint:

- Upload PDF files  
- Extract text  
- Split into chunks  
- Generate embeddings  
- Store in vector database  

---

## Ask Questions (RAG Pipeline)

Use the `/ask` endpoint.

### Example Queries

- What is the role about?  
- What skills are required?  

### System Flow

- Convert query to embedding  
- Retrieve relevant chunks from vector DB  
- Inject context into LLM prompt  
- Generate answer using retrieved knowledge  
- Return answer with source attribution  

---

## Conversational Memory

Supports multi-turn chat:

```
User: What is the role about?
User: What skills are required?
```

System behavior:

- Maintains chat history  
- Uses prior context  
- Produces coherent follow-up answers  

---

## Clear Chat History

```
POST /clear-history
```

---

## Logging & Monitoring

Logs stored in:

```
logs/app.log
```

Tracks:

- User queries  
- System actions  
- Errors  

---

## Full Demo Flow

1. Upload a document  
2. Ask a question  
3. Observe retrieved sources  
4. Ask follow-up questions  
5. Verify context-aware answers  
6. Check logs for system behavior  

---

## Core Pipeline

```
Document → Chunking → Embeddings → Vector DB
Query → Embedding → Retrieval → Context → LLM → Answer
Memory → Multi-turn conversation
```

---

## Real vs Heuristic Components

### Real Implementations

- Semantic search using embeddings  
- Vector database retrieval (Chroma)  
- LLM-based answer generation  
- Source-grounded responses  
- Conversational memory  

### Heuristic / Simplified

- Chunk size and overlap tuning  
- Basic ranking strategy (no re-ranker)  
- Single embedding model  

---

## Best Demo Mode

For best results:

- Use well-structured PDFs  
- Ask specific queries  
- Use follow-up questions to test memory  
- Verify source attribution  

---

## Technologies Used

- Python  
- FastAPI  
- SentenceTransformers  
- ChromaDB  
- OpenAI / GPT  
- REST APIs  

---

## Future Improvements

- Hybrid search (BM25 + vector search)  
- Re-ranking with cross-encoders  
- Streaming responses  
- Async ingestion pipeline  
- Frontend chat UI  
- Redis-based memory  
- RAG evaluation metrics  

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed updates.

---

## Support

If you found this project useful, consider giving it a star on GitHub.
