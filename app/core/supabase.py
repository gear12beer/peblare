from supabase import Client, create_client

from app.core.config import (
    SUPABASE_KEY,
    SUPABASE_URL,
)

supabase: Client = create_client(
    supabase_key=SUPABASE_KEY,
    supabase_url=SUPABASE_URL,
)