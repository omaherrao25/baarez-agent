from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
import models
from schemas import PromptRequest, AgentResponse
from tools import tool_save_memory, tool_get_memory, tool_calculate, route_prompt

Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/agent/query", response_model=AgentResponse)
def agent_query(request: PromptRequest, db: Session = Depends(get_db)):

    tool, input1, input2 = route_prompt(request.prompt)

    if tool == "memory_save":
        result = tool_save_memory(db, input1, input2)

    elif tool == "memory_read":
        result = tool_get_memory(db, input1)

    elif tool == "calculator":
        result = tool_calculate(input1)

    else:
        return {"error": "I do not have a tool for that."}

    return {
        "original_prompt": request.prompt,
        "chosen_tool": tool,
        "tool_input": input1,
        "response": result
    }
