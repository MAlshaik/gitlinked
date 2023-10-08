from content_recommendation import recommend_repos_for_user, recommend_users_for_repo, SupabaseContentDatabase, test
from dotenv import load_dotenv




def get_repositories_for_user_by_content(user_id: str):
    """
    Given a user id, return a list of repositories that are recommended
    based on the user's description and skills, and the textual content of the repositories
    using semantic similarity
    """
    db = SupabaseContentDatabase()
    recommendations = recommend_repos_for_user(user_id, db)
    return recommendations







def get_network_recommendations_for_user(user_id):
    '''
    Given a user id, return a list of repositories that are recommended
    based on the network of users and repositories surrounding that user
    using the graph embedding approach
    '''
    db = SupabaseContentDatabase()
    users = db.get_all_items("user")
    repositories = db.get_all_items("repository")

    
    




if __name__ == "__main__":
    




    # load_dotenv()

    # result = get_repositories_for_user_by_content({
    #     "id": "computer science guy",
    #     "description": "I work with Apollo 11 guidance systems",
    #     "skills": "python, javascript"
    # })


    # print(result)



