import os
from supabase import create_client, Client


class SupabaseDatabase:

    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_ANON_KEY")
        self.client: Client = create_client(url, key)

        self.all_repos = []
        self.all_users = []



    def get_all_users(self): 
        if (len(self.all_users) > 0):
            return self.all_users
        self.all_users = self.client.table("users_descriptive").select("*").execute().data
        return self.all_users



    def get_all_repos(self):
        if (len(self.all_repos) > 0):
            return self.all_repos
        self.all_repos = self.client.table("repo").select("*").execute().data
        return self.all_repos


