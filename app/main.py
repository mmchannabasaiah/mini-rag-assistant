from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Mini RAG Assistant",
    description="A small RAG application",
    version="1.0.0",
)

app.include_router(router)