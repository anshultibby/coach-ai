from supabase import create_client, Client
from functools import lru_cache

from app.core.config import settings

@lru_cache()
def get_supabase() -> Client:
    """
    Create a Supabase client instance.
    Uses lru_cache to maintain a single instance throughout the application.
    """
    return create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_KEY
    )

# Create a global client instance
supabase = get_supabase() 