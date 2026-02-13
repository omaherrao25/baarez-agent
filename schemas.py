from pydantic import BaseModel
from typing import Optional, Dict, Any

class PromptRequest(BaseModel):
    prompt: str


class ToolResponse(BaseModel):
    result: Optional[Any] = None
    key: Optional[str] = None
    value: Optional[str] = None
    status: Optional[str] = None
    error: Optional[str] = None


class AgentResponse(BaseModel):
    original_prompt: str
    chosen_tool: str
    tool_input: Optional[str]
    response: Dict[str, Any]
