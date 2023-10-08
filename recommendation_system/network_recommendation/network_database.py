import typing as t
from network_recommender import GraphRelationship
from recommendation_system.supabase_base import SupabaseDatabase


class SupabaseNetworkDatabase:


    def __init__(self):
        self.db = SupabaseDatabase()
        self.client = self.db.client


    def get_all_user_ids(self) -> t.List[str]:
        return 
    
    def get_all_repository_ids(self) -> t.List[str]:
        pass
    
    def get_all_tag_ids(self) -> t.List[str]:
        pass

    def get_all_relationships(self) -> t.List[GraphRelationship]:
        pass


