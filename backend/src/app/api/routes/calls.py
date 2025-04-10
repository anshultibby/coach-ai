from fastapi import APIRouter, HTTPException, Request
from twilio.twiml.voice_response import VoiceResponse
from twilio.request_validator import RequestValidator
from pydantic import BaseModel
from typing import Optional

from app.core.config import settings
from app.core.supabase import supabase

router = APIRouter()

class SpeechInput(BaseModel):
    CallSid: str
    From: str
    SpeechResult: str

def validate_twilio_request(request: Request) -> bool:
    validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)
    # Get the request URL and POST data
    # You might need to adjust this based on your actual request structure
    return True  # TODO: Implement proper validation

@router.post("/incoming")
async def handle_incoming_call(request: Request):
    """Handle incoming calls from Twilio"""
    if not validate_twilio_request(request):
        raise HTTPException(status_code=403, detail="Invalid Twilio request")
    
    response = VoiceResponse()
    # Start gathering speech input
    gather = response.gather(
        input='speech',
        action='/api/calls/process-speech',
        language='en-US',
        speechTimeout='auto'
    )
    gather.say("Hello! I'm your AI health coach. How can I help you today?")
    
    return response.to_xml()

@router.post("/process-speech")
async def process_speech(speech_input: SpeechInput):
    """Process speech input from Twilio and return TwiML response"""
    try:
        # Find or create user based on phone number
        user_response = supabase.table('users').select("*").eq('phone_number', speech_input.From).execute()
        if not user_response.data:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_id = user_response.data[0]['id']
        
        # Get or create session
        session_response = supabase.table('sessions').select("*").eq('user_id', user_id).order('created_at', desc=True).limit(1).execute()
        
        # Create new message
        message_data = {
            'session_id': session_response.data[0]['id'],
            'role': 'user',
            'content': speech_input.SpeechResult
        }
        supabase.table('messages').insert(message_data).execute()
        
        # TODO: Process with OpenAI and get response
        ai_response = "I understand you said: " + speech_input.SpeechResult
        
        # Store AI response
        ai_message_data = {
            'session_id': session_response.data[0]['id'],
            'role': 'assistant',
            'content': ai_response
        }
        supabase.table('messages').insert(ai_message_data).execute()
        
        # Return TwiML response
        response = VoiceResponse()
        gather = response.gather(
            input='speech',
            action='/api/calls/process-speech',
            language='en-US',
            speechTimeout='auto'
        )
        gather.say(ai_response)
        
        return response.to_xml()
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/hangup")
async def handle_hangup(request: Request):
    """Handle call hangup webhook from Twilio"""
    if not validate_twilio_request(request):
        raise HTTPException(status_code=403, detail="Invalid Twilio request")
    
    # TODO: Implement call cleanup logic
    return {"status": "success"} 