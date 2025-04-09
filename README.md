# AI Voice Health Coach

A personalized AI-powered voice health coaching system that provides real-time health guidance and support through phone calls.

## System Architecture

### Core Components

1. **Voice Interface Layer**
   - Twilio integration for handling phone calls
   - Voice-to-text and text-to-voice conversion
   - Call session management

2. **AI Engine Layer**
   - Abstracted AI provider interface (currently using OpenAI)
   - Conversation context management
   - Health coaching logic and prompts
   - Extensible design for future AI provider integrations

3. **Data Layer**
   - Supabase (PostgreSQL) database
   - User profiles and preferences
   - Conversation history
   - Health metrics and progress tracking

4. **Backend Service**
   - FastAPI backend
   - Async endpoint handling
   - Automatic OpenAPI/Swagger documentation
   - Type-safe with Pydantic models
   - Docker containerization

### Data Flow

1. User initiates a call to the Twilio number
2. Voice input is converted to text
3. Backend processes the input and maintains conversation context
4. AI engine generates appropriate responses
5. Response is converted back to voice and delivered to user
6. Conversation data is stored in Supabase

### Key Features

- Real-time voice conversations with AI health coach
- Personalized health guidance and recommendations
- Progress tracking and goal setting
- Secure data storage and user privacy
- Scalable and modular architecture
- Easy integration with different AI providers

## Technical Stack

- **Backend**: Python 3.11+, FastAPI
- **AI Provider**: OpenAI (with abstraction layer for flexibility)
- **Database**: Supabase (PostgreSQL)
- **Voice Services**: Twilio
- **Infrastructure**: Docker, Docker Compose
- **API Documentation**: OpenAPI/Swagger (auto-generated)

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Twilio Account and Phone Number
- OpenAI API Key
- Supabase Project
- Python 3.11 or higher (for local development)

### Environment Variables

```env
# AI Provider
AI_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key

# Twilio
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key

# Server
PORT=8000
ENVIRONMENT=development
```

### Running with Docker

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your credentials
3. Run `docker-compose up -d`
4. Access the API at `http://localhost:8000`
5. View API documentation at `http://localhost:8000/docs`

## Development

### Project Structure

```
.
├── backend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py        # FastAPI application
│   │   │   ├── core/          # Core configurations
│   │   │   ├── api/           # API routes
│   │   │   ├── models/        # Pydantic models
│   │   │   ├── schemas/       # Database schemas
│   │   │   ├── services/      # Business logic
│   │   │   └── utils/         # Helper functions
│   │   └── tests/             # Test files
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pyproject.toml
├── docker-compose.yml
└── README.md
```

### API Endpoints

- `POST /api/v1/calls/incoming` - Handle incoming Twilio calls
- `POST /api/v1/calls/status` - Handle call status updates
- `GET /api/health` - Health check endpoint

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload --port 8000
```

## Contributing

[Contributing guidelines]

## License

MIT License
