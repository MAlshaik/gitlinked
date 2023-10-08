from recommendation_system.content_recommendation.use_content_recommender import User, Repository
from content_recommender import RecommendableItem, ContentDatabase
import typing as t
from recommendation_system.supabase_base import SupabaseDatabase


class SupabaseContentDatabase(ContentDatabase):

    def __init__(self):
        super().__init__()
        self.db = SupabaseDatabase()
        self.client = self.db.client


    def get_all_items(self, type: str) -> t.List[RecommendableItem]:
        if type == "user":
            return self.get_users()
        elif type == "repository":
            return self.get_repositories()
        

    def get_item(self, type: str, item_id: str) -> RecommendableItem:
        if type == "user":
            return self.get_user(item_id)
        elif type == "repository":
            return self.get_repository(item_id)


    def get_users(self) -> t.List[User]:
        users = self.client.table("users").select("*").execute().data
        return [User(i) for i in users]

    def get_repositories(self) -> t.List[Repository]:
        repositories = self.client.table("repo").select("*").execute().data
        return [Repository(i) for i in repositories]


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
    



