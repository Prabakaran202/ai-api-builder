from fastapi import APIRouter
from app.agent import generate_api
from app.generator import create_project

router = APIRouter()


@router.post("/generate-api")
def generate(prompt: str):

    code = generate_api(prompt)

    project = create_project("generated_api", code)

    return {
        "message": "API project generated",
        "project": project
    }
