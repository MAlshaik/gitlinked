from get_recommendations import User, Repository
from database import Supabase
from dotenv import load_dotenv


def get_repositories_for_user(user_data):
    db = Supabase()
    content_recommendations =  User(user_data, db).get_repository_matches()
    return content_recommendations





if __name__ == "__main__":
    
    load_dotenv()

    result = get_repositories_for_user({
        "id": "computer science guy",
        "description": "I work with assembly",
        "skills": "python, javascript"
    })


    print(result)



