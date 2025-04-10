from fastapi import APIRouter, HTTPException
from typing import List

from app.models.assistants import Assistant, AssistantResponse
from app.crud import assistants

router = APIRouter()

@router.post("/", response_model=AssistantResponse)
async def create_assistant(assistant: Assistant):
    """Create a new assistant with name and prompt"""
    try:
        return assistants.create_assistant(assistant)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{assistant_id}", response_model=AssistantResponse)
async def get_assistant(assistant_id: str):
    """Get an assistant by ID"""
    try:
        assistant = assistants.get_assistant(assistant_id)
        if not assistant:
            raise HTTPException(status_code=404, detail="Assistant not found")
        return assistant
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[AssistantResponse])
async def list_assistants():
    """List all assistants"""
    try:
        return assistants.list_assistants()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{assistant_id}", response_model=AssistantResponse)
async def update_assistant(assistant_id: str, assistant: Assistant):
    """Update an assistant's name and prompt"""
    try:
        updated = assistants.update_assistant(assistant_id, assistant)
        if not updated:
            raise HTTPException(status_code=404, detail="Assistant not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 