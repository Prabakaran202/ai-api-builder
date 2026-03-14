from fastapi import FastAPI
from routes import router

app = FastAPI(
    title= "AI API BUILDER",
    description= "GENERATE AI APIS USING  AI",
    version= "1.0"
)
app.include_router(router)
