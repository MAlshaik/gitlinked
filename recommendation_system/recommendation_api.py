from get_recommendations import User, Repository
from database import Supabase



def get_repositories_for_user(user_data):
    db = Supabase()
    User(user_data, db).get_repository_matches()

