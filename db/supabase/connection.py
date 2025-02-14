import os
from dotenv import load_dotenv
from supabase import create_client, Client

def get_supabase_connection() -> Client:
    """Create and return a Supabase client"""

    load_dotenv()
    
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Supabase URL and Key must be set in environment variables")
    
    return create_client(url, key)