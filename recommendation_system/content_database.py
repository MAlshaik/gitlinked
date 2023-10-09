import typing as t
from use_content_recommender import User, Repository
from content_recommender import RecommendableItem, GeneralContentDatabase
from supabase_base import SupabaseDatabase



class SupabaseContentDatabase(GeneralContentDatabase):

    def __init__(self):
        super().__init__()
        self.db = SupabaseDatabase()
        self.client = self.db.client


    def get_all_items(self, type: str) -> t.List[RecommendableItem]:
        if type == "user":
            return self.get_recommendable_users()
        elif type == "repository":
            return self.get_recommendable_repositories()
        

    def get_item(self, type: str, item_id: str) -> RecommendableItem:
        if type == "user":
            return self.get_user(item_id)
        elif type == "repository":
            return self.get_repository(item_id)


    def get_recommendable_users(self) -> t.List[User]:
        result = [User(i) for i in self.get_all_users()]
        return result

    def get_recommendable_repositories(self) -> t.List[Repository]:
        return [Repository(i) for i in self.get_all_repos()]


    def get_user(self, user_id) -> User:
        user_data = self.client.table("users_descriptive").select("*").eq("id", user_id).execute().data[0]
        return User(user_data)


    def save_user_description_embedding(self, user_id, embedding):
        pass
    
    def get_repository(self, repository_id) -> Repository:
        repository_data = self.client.table("repo").select("*").eq("id", repository_id).execute().data[0]
        return Repository(repository_data)

    def save_repository_description_embedding(self, repository_id, embedding):
        pass
    



