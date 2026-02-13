import re
from sqlalchemy.orm import Session
from models import Memory

# SAVE MEMORY
def tool_save_memory(db: Session, key: str, value: str):
    obj = db.query(Memory).filter(Memory.key == key).first()

    if obj:
        obj.value = value
    else:
        obj = Memory(key=key, value=value)
        db.add(obj)

    db.commit()
    return {"key": key, "value": value, "status": "saved"}


# GET MEMORY
def tool_get_memory(db: Session, key: str):
    obj = db.query(Memory).filter(Memory.key == key).first()
    if obj:
        return {"key": key, "value": obj.value}
    return {"key": key, "value": None}


# CALCULATOR
def tool_calculate(expression: str):
    try:
        result = eval(expression)
        return {"result": result}
    except:
        return {"error": "Invalid expression"}


# ROUTER
def route_prompt(prompt: str):
    p = prompt.lower()

    if "remember" in p:
        match = re.search(r"remember my (.*) is (.*)", p)
        if match:
            return "memory_save", match.group(1), match.group(2)

    if "what is my" in p:
        match = re.search(r"what is my (.*)\?", p)
        if match:
            return "memory_read", match.group(1), None

    if "what is" in p:
        expr = (
            p.replace("what is", "")
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("divided by", "/")
        )
        return "calculator", expr.strip(), None

    return None, None, None
