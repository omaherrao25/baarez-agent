# Baarez Backend POC

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

## Testing API

Open Swagger UI:

http://127.0.0.1:8000/docs

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

