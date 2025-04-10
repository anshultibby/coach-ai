# AI Health Coach Architecture

## Overview
An AI-powered health coach system that allows users to have phone conversations with an AI coach. The system uses Twilio for phone interactions, OpenAI for intelligence, and PostgreSQL for data storage.

## Key Design Decisions

### 1. Voice Interaction Approach
We chose Twilio's TwiML Voice API over WebSocket-based Media Streams because:
- Simpler implementation
- More cost-effective
- Built-in STT/TTS capabilities
- Easier maintenance and debugging
- Better reliability with fewer moving parts

### 2. System Architecture

```
/coach-ai
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── calls.py          # Twilio voice endpoints
│   │   │   ├── dashboard.py      # Web dashboard endpoints
│   │   │   └── users.py          # User management
│   │   └── services/
│   │   │   ├── ai/
│   │   │   │   ├── llm.py           # OpenAI integration
│   │   │   │   └── context.py       # Conversation context
│   │   │   └── call_manager.py      # Call flow orchestration
│   │   └── models/
│   │   │   ├── database.py          # SQLAlchemy models
│   │   │   └── schemas.py           # Pydantic models
│   │   └── core/
│   │   │   ├── config.py            # Environment & app config
│   │   │   ├── database.py          # Database connection
│   │   │   └── logger.py            # Logging setup
│   ├── migrations/                  # Database migrations
│   └── plans/                      # Architecture & planning docs
└── tests/                      # Test suite
```

### 3. Database Schema
- users: Store user information
- sessions: Track conversation sessions
- messages: Store conversation history
- assistants: Configure AI personalities

### 4. Call Flow
1. User calls Twilio phone number
2. Twilio sends webhook to `/call/incoming`
3. System responds with TwiML gather command
4. User speaks, Twilio converts to text
5. Text sent to `/call/process-speech`
6. System:
   - Creates/updates session
   - Stores user message
   - Gets conversation context
   - Gets AI response via OpenAI
   - Stores AI response
   - Returns TwiML with response
7. Cycle repeats from step 3

### 5. Implementation Steps

#### Phase 1: Basic Setup
1. Set up FastAPI application structure
2. Implement database models
3. Create basic Twilio endpoints
4. Add OpenAI integration

#### Phase 2: Core Features
1. Implement conversation context management
2. Add user authentication
3. Create session management
4. Implement basic error handling

#### Phase 3: Dashboard
1. Create admin dashboard routes
2. Implement conversation viewing
3. Add basic analytics
4. Create assistant configuration UI

## Technology Stack
- FastAPI: Web framework
- PostgreSQL: Database
- SQLAlchemy: ORM
- Twilio: Voice interface
- OpenAI: LLM provider
- Pydantic: Data validation
- Alembic: Database migrations

## Environment Variables
```
DATABASE_URL=postgresql://...
OPENAI_API_KEY=sk-...
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
TWILIO_PHONE_NUMBER=+1...
```

## Next Steps
1. Set up basic FastAPI application
2. Implement database models
3. Create Twilio endpoints
4. Add OpenAI integration 