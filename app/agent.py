import os
from dotenv import load_dotenv
from google import genai  # ← different import


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_api(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt  # ← 'contents' not 'input'
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while generating the API."
if __name__ == "__main__":
    user_prompt = input("Enter a description for the API you want to generate: ")
    api_code = generate_api(user_prompt)
    print("\nGenerated API Code:\n")
    print(api_code)