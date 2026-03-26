from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="AI Knowledge Copilot",
    description="RAG-based enterprise assistant",
    version="1.0.0"
)

# Include all routes from api layer
app.include_router(router)
