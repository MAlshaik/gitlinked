import os
from supabase import create_client, Client


class SupabaseDatabase:

    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_ANON_KEY")
        self.client: Client = create_client(url, key)



