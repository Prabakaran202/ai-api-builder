from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes import router
import os

app = FastAPI(
    title="AI API Builder 🤖",
    description="Generate FastAPI backends from natural language prompts using Gemini AI",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router
app.include_router(router)

# Root endpoint
@app.get("/api")
def root():
    return {
        "msg": "AI API Builder Running! 🚀",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Static files — LAST-ல mount பண்ணு!
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "app/static")
app.mount("/", StaticFiles(directory=STATIC_DIR,html=True), name="static")
