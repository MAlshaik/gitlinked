from content_database import SupabaseContentDatabase
from network_database import SupabaseNetworkDatabase
from use_content_recommender import recommend_users_for_repo, recommend_repos_for_user, User, Repository, content_test
from use_network_recommender import network_test, find_close_items
from dotenv import load_dotenv
import sys, os



def get_repositories_for_user_by_content(user_id: str, search_prompt: str = None):
    """
    Given a user id, return a list of repositories that are recommended
    based on the user's description and skills, and the textual content of the repositories
    using semantic similarity
    """
    db = SupabaseContentDatabase()
    recommendations = recommend_repos_for_user(user_id, db, search_prompt)
    return recommendations



def get_users_for_repository_by_content(repository_id: str):
    """
    Given a repository id, return a list of users that are recommended
    based on the user's description and skills, and the textual content of the repositories
    using semantic similarity
    """
    db = SupabaseContentDatabase()
    recommendations = recommend_users_for_repo(repository_id, db)
    return recommendations




def get_network_recommendations_for_item(user_id: str, item_type: str):
    '''
    Given a user id, return a list of repositories that are recommended
    based on the network of users and repositories surrounding that user
    using the graph embedding approach
    '''
    db = SupabaseNetworkDatabase()
    result = find_close_items(db, user_id, item_type)

    return result




def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


if __name__ == "__main__":
    load_dotenv()

    # result = get_repositories_for_user_by_content("113369108")
    # result = get_users_for_repository_by_content("2")
    
    result = get_network_recommendations_for_item("113369108", "user")

    print(result)


