from content_database import SupabaseContentDatabase
from network_database import SupabaseNetworkDatabase
from use_content_recommender import recommend_users_for_repo, recommend_repos_for_user, User, Repository, content_test
from content_recommendation import ContentRecommender
from use_network_recommender import find_close_items
from dotenv import load_dotenv
import sys, os



def get_repositories_for_user_by_content(
    user_id: str,
    account_for_user_features: list = ["description", "interest", "skills"], 
    account_for_repo_features: list = ["description", "languages"]
):

    """
    Given a user id, return a list of repositories that are recommended
    based on the user's description and skills, and the textual content of the repositories
    using semantic similarity
    """
    db = SupabaseContentDatabase()
    
    user = db.get_item("user", user_id)
    return ContentRecommender(db).recommend_items_for_item(
        user, "repository", 
        account_for_user_features, account_for_repo_features)




def get_users_for_repository_by_content(
    repository_id: str, 
    account_for_repo_features: list = ["description", "languages"],
    account_for_user_features: list = ["description", "interest", "skills"],
):
    """
    Given a repository id, return a list of users that are recommended
    based on the user's description and skills, and the textual content of the repositories
    using semantic similarity
    """
    db = SupabaseContentDatabase()
    repository = db.get_item("repository", repository_id)
    return ContentRecommender(db).recommend_items_for_item(
        repository, "user", 
        account_for_user_features, account_for_repo_features)




def get_network_recommendations_for_item(user_id: str, item_type: str):
    '''
    Given a user id, return a list of recommended repos and users based on 
    the network of users and repositories surrounding that user
    using the graph embedding approach
    '''
    db = SupabaseNetworkDatabase()
    top_repositories, top_users = find_close_items(db, user_id, item_type)

    return top_repositories, top_users




def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


if __name__ == "__main__":
    load_dotenv()

    # result = get_repositories_for_user_by_content("113369108")
    # result = get_users_for_repository_by_content("2")
    
    result = get_network_recommendations_for_item("113369108", "user")

    print(result[0])
    print(result[1])


