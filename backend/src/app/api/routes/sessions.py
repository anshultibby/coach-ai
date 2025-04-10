from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from app.core.supabase import supabase

router = APIRouter()

class MessageCreate(BaseModel):
    role: str  # 'user' | 'assistant' | 'system'
    content: str

class MessageResponse(MessageCreate):
    id: str
    session_id: str
    created_at: datetime

class SessionCreate(BaseModel):
    user_id: str
    assistant_id: str

class SessionResponse(SessionCreate):
    id: str
    start_time: datetime
    created_at: datetime

@router.post("/", response_model=SessionResponse)
async def create_session(session: SessionCreate):
    try:
        response = supabase.table('sessions').insert(session.model_dump()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(session_id: str):
    try:
        response = supabase.table('sessions').select("*").eq('id', session_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Session not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{session_id}/messages", response_model=List[MessageResponse])
async def get_session_messages(session_id: str):
    try:
        response = supabase.table('messages').select("*").eq('session_id', session_id).order('created_at').execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{session_id}/messages", response_model=MessageResponse)
async def create_message(session_id: str, message: MessageCreate):
    try:
        data = message.model_dump()
        data['session_id'] = session_id
        response = supabase.table('messages').insert(data).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{user_id}", response_model=List[SessionResponse])
async def get_user_sessions(user_id: str):
    try:
        response = supabase.table('sessions').select("*").eq('user_id', user_id).order('created_at', desc=True).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 