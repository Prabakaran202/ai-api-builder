from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="AI API Builder",
    description="Generate FastAPI APIs using AI",
    version="1.0"
)

app.include_router(router)
