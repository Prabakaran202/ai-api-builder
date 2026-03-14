from fastapi import APIRouter
from agent import generate_api

router = APIRouter()

@router.post("/generate-api")
def create_api(prompt:str):
    api_code = generate_api(prompt)
    return {"api_code": api_code}
