import re
from sqlalchemy.orm import Session
from models import Memory

# SAVE MEMORY
def tool_save_memory(db: Session, key: str, value: str):
    obj = db.query(Memory).filter(Memory.key == key).first() # query to check key already exists in DB

    if obj:
        obj.value = value # Update stored memory
    else:
        obj = Memory(key=key, value=value) # Create new memory
        db.add(obj)

    db.commit() # Save changes to DB permanently
    return {"key": key, "value": value, "status": "saved"} # Provides structured response API output


# GET MEMORY
def tool_get_memory(db: Session, key: str):
    obj = db.query(Memory).filter(Memory.key == key).first()
    if obj:
        return {"key": key, "value": obj.value}
    return {"key": key, "value": None} # Return None if key not found, allows agent to handle missing memory gracefully


# CALCULATOR
def tool_calculate(expression: str):
    try:
        result = eval(expression) # Evaluate the math expression
        return {"result": result}
    except:
        return {"error": "Invalid expression"}


# ROUTER
def route_prompt(prompt: str):
    p = prompt.lower()

    if "remember" in p:
        match = re.search(r"remember my (.*) is (.*)", p) # Extract key and value from prompt using regex
        if match:
            return "memory_save", match.group(1), match.group(2) # Return tool name and extracted key/value for memory saving

    if "what is my" in p: # Detect memory recall intent
        match = re.search(r"what is my (.*)\?", p)
        if match:
            return "memory_read", match.group(1), None

    if "what is" in p: # Detect calculator intent
        expr = (
            p.replace("what is", "")
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("divided by", "/")
        )
        return "calculator", expr.strip(), None

    return None, None, None
