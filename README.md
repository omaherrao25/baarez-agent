# Baarez AI Agent Backend

A FastAPI-based AI Agent service that routes user prompts to appropriate tools (Calculator and Memory).

---

## Project Structure

```
baarez-agent/
│
├── main.py # FastAPI app entry point and endpoint definitions
├── database.py # Database connection and session setup
├── models.py # SQLAlchemy ORM models (Memory table)
├── schemas.py # Pydantic request/response models
├── tools.py # Tool logic (memory + calculator + router)
│
├── memory.sql # SQL CREATE TABLE script (as required)
├── memory.db # SQLite database (auto-created on run)
│
├── README.md # Project documentation
├── .gitignore # Ignore venv, cache, db files
│
└── venv/ # Virtual environment (not pushed to GitHub)
```

---

## Features

- **Calculator Tool**: Safely evaluates mathematical expressions using AST parsing
- **Memory Tool**: Persistent key-value storage with SQLite/PostgreSQL support
- **Agent Router**: Rule-based intent detection and entity extraction
- **RESTful API**: Clean FastAPI endpoints with automatic OpenAPI documentation

---

## Tech Stack

- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

---

## Setup

1. Create virtual environment

python -m venv venv
venv\Scripts\activate

2. Install dependencies

pip install fastapi uvicorn sqlalchemy pydantic

---

## Run Server

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

---

## Database

memory.sql contains CREATE TABLE statement.

SQLite DB auto-created as memory.db.

---

## API Documentation

Once running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

---

### Calculator

"What is 10 plus 5"

---

### Save Memory

"Remember my cat's name is Fluffy"

---

### Recall Memory

"What is my cat's name?"

---

## Architecture Decisions

### Why Rule-Based Routing?

| Rule-Based | LLM-Based |
|------------|-----------|
| Deterministic | Probabilistic |
| Fast (no API calls) | Slow (API latency) |
| Free | Costly per request |
| Works offline | Requires connectivity |
| Easy to debug | Black box |

For this POC with well-defined intents, rule-based is appropriate. For complex, ambiguous queries, consider upgrading to LangChain/LLM.

### Why Pydantic?

- Automatic request validation
- Type coercion and conversion
- Clear error messages
- OpenAPI schema generation
- IDE autocomplete support

### Why SQLAlchemy?

- Database-agnostic (SQLite for POC, PostgreSQL for production)
- ORM prevents SQL injection
- Easy migration path with Alembic
- Connection pooling for production