
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from get_recommendations import Database


class Supabase(Database):

    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_ANON_KEY")
        self.client: Client = create_client(url, key)


    def get_user(self, user_id):
        self.client.table("users").select("*").eq("id", user_id).execute()


    def save_user_description_embedding(self, user_id, embedding):
        pass
    
    def get_repository(self, repository_id):
        pass


    def save_repository_description_embedding(self, repository_id, embedding):
        pass
    

    def get_users(self):
        pass
    
    def get_repositories(self):
        pass