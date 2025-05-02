from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import users, calls, sessions, assistants

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(calls.router, prefix="/api/calls", tags=["calls"])
app.include_router(sessions.router, prefix="/api/sessions", tags=["sessions"])
app.include_router(assistants.router, prefix="/api/assistants", tags=["assistants"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"} 