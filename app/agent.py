import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"

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

# === models.py ===
- SQLAlchemy ORM models
- All necessary columns with types

# === schemas.py ===
- Pydantic schemas for request/response
- Create, Update, Response schemas

# === routes.py ===
- All CRUD endpoints (GET, POST, PUT, DELETE)
- Proper HTTPException error handling
- Depends(get_db) for database session

IMPORTANT: Separate each file exactly like this:
# === main.py ===
<code here>

# === database.py ===
<code here>

Return ONLY raw Python code. No markdown, no backticks, no explanation."""

def validate_code(code: str) -> bool:
    required = ["from fastapi", "FastAPI(", "def "]
    return any(keyword in code for keyword in required)

def generate_api(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Create: {prompt}"}
            ],
            temperature=0.3,
            max_tokens=4096
        )

        code = response.choices[0].message.content.strip()

        # Clean backticks if model adds them
        if code.startswith("```"):
            code = code.split("\n", 1)[-1]
        if code.endswith("```"):
            code = code.rsplit("```", 1)[0]

        code = code.strip()

        if not validate_code(code):
            raise Exception("Generated code looks invalid!")

        return code

    except Exception as e:
        raise Exception(f"Groq failed: {str(e)}")