from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import Optional

from app.core.supabase import supabase

router = APIRouter()

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    dob: date
    phone_number: str
    email: str

class UserResponse(UserCreate):
    id: str

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    try:
        response = supabase.table('users').insert(user.model_dump()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{phone_number}")
async def get_user_by_phone(phone_number: str):
    try:
        response = supabase.table('users').select("*").eq('phone_number', phone_number).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 