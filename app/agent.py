import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

SYSTEM_PROMPT = """You are a FastAPI expert developer.
Generate a COMPLETE FastAPI project with ALL of these files:

# === main.py ===
- FastAPI app setup with CORS
- Include all routers
- Uvicorn entry point

# === database.py ===
- SQLAlchemy engine setup
- SQLite database
- SessionLocal and Base

# === models.py ===s
- SQLAlchemy ORM models
- All necessary columns with types

# === schemas.py ===
- Pydantic schemas for request/response
- Create, Update, Response schemas

# === routes.py ===
- All CRUD endpoints (GET, POST, PUT, DELETE)
- Proper HTTPException error handling
- Depends(get_db) for database session

Requirements:
- Add helpful comments in each file
- Use proper type hints
- Production-ready code

<<<<<<< HEAD
Return ONLY raw Python code.
No markdown, no explanation, no backticks.
"""
def validate_code(code: str) -> bool:
<<<<<<< HEAD
    required = ["from fastapi", "FastAPI(", "def "]
=======
    required = ["from fastapi", "def "]
>>>>>>> 24483fe (newnew)
=======
IMPORTANT: Separate each file exactly like this:
# === main.py ===
<code here>

# === database.py ===
<code here>

# === models.py ===
<code here>

# === schemas.py ===
<code here>

# === routes.py ===
<code here>

Return ONLY raw Python code. No markdown, no backticks, no explanation."""

def validate_code(code: str) -> bool:
    required = ["from fastapi", "FastAPI(", "def "]
>>>>>>> f62253e (ne)
    return any(keyword in code for keyword in required)

def generate_api(prompt: str) -> str:
    full_prompt = f"{SYSTEM_PROMPT}\n\nUser request: {prompt}"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": full_prompt,
                "stream": False
            },
            timeout=400
        )

        if response.status_code != 400:
            raise Exception(f"Ollama error: {response.status_code}")

        code = response.json().get("response", "").strip()

        # Clean markdown backticks if model adds them
        if code.startswith("```"):
            code = code.split("\n", 1)[-1]
        if code.endswith("```"):
            code = code.rsplit("```", 1)[0]

        code = code.strip()

        if not validate_code(code):
            raise Exception("Generated code looks invalid!")

        return code

    except requests.exceptions.ConnectionError:
        raise Exception("Ollama not running! Start with: ollama serve")

    except Exception as e:
        raise Exception(f"Generation failed: {str(e)}")