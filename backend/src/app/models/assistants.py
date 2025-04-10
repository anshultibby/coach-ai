from pydantic import BaseModel

class Assistant(BaseModel):
    name: str
    prompt: str

class AssistantResponse(Assistant):
    id: str 