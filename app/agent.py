import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
<<<<<<< HEAD
    required = ["from fastapi", "FastAPI(", "def "]
=======
    required = ["from fastapi", "def "]
>>>>>>> 24483fe (newnew)
    return any(keyword in code for keyword in required)

def generate_api(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": SYSTEM_PROMPT.format(prompt=prompt)
                }
            ]
        )
        code = response.choices[0].message.content.strip()

        if not validate_code(code):
            raise Exception("Generated code invalid!")

        return code

    except Exception as e:
        raise Exception(f"Groq failed! Error: {e}")