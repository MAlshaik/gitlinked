from get_recommendations import User, Repository, recommend_repos_for_user, recommend_users_for_repo
from database import Supabase
from dotenv import load_dotenv




def get_repositories_for_user(user_data):
    db = Supabase()
    recommendations = recommend_repos_for_user(User(user_data), db)
    return recommendations.loc[recommendations["match_score"] > 0.3].to_dict("records")



def get_network_recommendations_for_user(user_id):
    pass



if __name__ == "__main__":
    
    load_dotenv()

    result = get_repositories_for_user({
        "id": "computer science guy",
        "description": "I work with Apollo 11 guidance systems",
        # "skills": "python, javascript"
    })


    print(result)



