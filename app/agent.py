import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
]

SYSTEM_PROMPT = """
You are a FastAPI expert developer.
Generate a complete, production-ready FastAPI endpoint.

User request: {prompt}

Requirements:
- Include all necessary imports
- Add Pydantic models with Field validation
- Add proper HTTPException error handling
- Add CRUD operations if needed
- Add helpful comments

Return ONLY raw Python code.
No markdown, no explanation, no backticks.
"""

def validate_code(code: str) -> bool:
    required = ["from fastapi", "FastAPI()", "def "]
    return any(keyword in code for keyword in required)

def generate_api(prompt: str) -> str:
    last_error = None

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=SYSTEM_PROMPT.format(prompt=prompt)
            )
            code = response.text.strip()

            # Validate generated code
            if not validate_code(code):
                continue

            return code

        except Exception as e:
            last_error = e
            continue

    raise Exception(f"All models failed! Last error: {last_error}")