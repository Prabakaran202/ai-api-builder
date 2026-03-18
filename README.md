AI API Builder 🚀

Prompt → Backend API in seconds

AI API Builder is an intelligent developer agent that converts natural language prompts into fully functional FastAPI backend APIs.

Built for the Gemini Live Agent Challenge, this project helps developers quickly generate CRUD APIs, database models, and project structure automatically using AI.

---

✨ Features

- 🧠 Natural language → FastAPI backend
- ⚡ Automatic CRUD API generation
- 🗄 Database model generation
- 📦 Ready-to-run project structure
- 🤖 Powered by Gemini AI
- 🧩 Developer productivity tool

---

🏗 Architecture

User Prompt
↓
FastAPI Backend
↓
Gemini AI Agent
↓
Code Generator
↓
Downloadable API Project

---

📂 Project Structure

ai-api-builder
│
├ app
│   ├ main.py
│   ├ agent.py
│   ├ generator.py
│   └ routes.py
│
├ generated_projects
│
├ requirements.txt
└ README.md

---

⚙ Tech Stack

- Python
- FastAPI
- Gemini AI API
- Uvicorn
- Docker (optional)

---

🚀 Example

User Prompt:

Create API for a todo application with title, description and status

Generated API:

- "POST /todos"
- "GET /todos"
- "PUT /todos/{id}"
- "DELETE /todos/{id}"

---

▶ Running the Project

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn app.main:app --reload

Open:
https://ai-api-builder.onrender.com

---

🎥 Demo

Demo video will show:

1. Entering prompt
2. AI generating backend
3. Downloading generated API project
4. Running the API

---

💡 Use Cases

- Rapid API prototyping
- Developer productivity
- Learning backend development
- Startup MVP building

---

🏆 Hackathon

Submitted to:

Gemini Live Agent Challenge

---

👨‍💻 Author

Prabakaran

---

⭐ Future Improvements

- Multi-database support
- Authentication generation
- Docker project export
- Microservice generation
