from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator
from agent import generate_api

router = APIRouter()

# ========================
# Request Model + Validation
# ========================
class PromptRequest(BaseModel):
    prompt: str = Field(
        min_length=10,
        max_length=500,
        description="Describe your API in natural language"
    )

    @field_validator("prompt")
    def validate_prompt(cls, v):
        # 1. Empty check
        if not v.strip():
            raise ValueError("Prompt cannot be empty!")

        # 2. API related words இருக்கணும்
        api_keywords = [
            "api", "create", "build", "make",
            "generate", "crud", "endpoint",
            "todo", "user", "product", "book"
        ]
        if not any(word in v.lower() for word in api_keywords):
            raise ValueError(
                "Prompt must be API related! "
                "Example: 'Create a todo API'"
            )

        # 3. Numbers மட்டும் இருக்க கூடாது
        if v.strip().isdigit():
            raise ValueError("Prompt cannot be only numbers!")

        return v.strip()

# ========================
# Response Model
# ========================
class ApiResponse(BaseModel):
    success: bool
    prompt: str
    api_code: str
    message: str

# ========================
# Route
# ========================
@router.post(
    "/api/generate",
    response_model=ApiResponse,
    summary="Generate FastAPI Code",
    description="Converts natural language to FastAPI backend"
)
def create_api(request: PromptRequest):
    try:
        api_code = generate_api(request.prompt)

        if not api_code:
            raise HTTPException(
                status_code=500,
                detail="API generation failed!"
            )

        return ApiResponse(
            success=True,
            prompt=request.prompt,
            api_code=api_code,
            message="API generated successfully! 🚀"
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error: {str(e)}"
        )