
import os
from supabase import create_client, Client
from get_recommendations import Database, User, Repository
import typing

class Supabase(Database):

    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_ANON_KEY")
        self.client: Client = create_client(url, key)


    def get_user(self, user_id) -> User:
        user_data = self.client.table("users").select("*").eq("id", user_id).execute().data[0]
        return User(user_data)


    def save_user_description_embedding(self, user_id, embedding):
        pass
    
    def get_repository(self, repository_id) -> Repository:
        repository_data = self.client.table("repo").select("*").eq("id", repository_id).execute().data[0]
        return Repository(repository_data)


    def save_repository_description_embedding(self, repository_id, embedding):
        pass
    

    def get_users(self) -> typing.List[User]:
        users = self.client.table("users").select("*").execute().data
        return [User(i) for i in users]
    
    def get_repositories(self) -> typing.List[Repository]:
        repositories = self.client.table("repo").select("*").execute().data
        return [Repository(i) for i in repositories]



