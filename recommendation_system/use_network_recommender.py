import typing as t
from network_recommender import get_most_similar_nodes, GraphNode, GraphRelationship
from network_database import SupabaseNetworkDatabase
import enum



class NodeType(enum.Enum):
    USER = "user"
    REPOSITORY = "repository"
    TAG = "tag"




def get_all_nodes(db: SupabaseNetworkDatabase) -> t.List[GraphNode]:
    all_users = [GraphNode(i, NodeType.USER.value) 
                for i in db.get_all_user_ids()]

    all_repositories = [GraphNode(i, NodeType.REPOSITORY.value) 
                        for i in db.get_all_repository_ids()]
    
    all_tags = [GraphNode(i, NodeType.TAG.value)
                for i in db.get_all_tag_ids()]

    return all_users + all_repositories + all_tags


def get_all_relationships(db: SupabaseNetworkDatabase) -> t.List[GraphRelationship]:
    # Get the relationships repositories and their top contributors

    all_repositories = db.all_repositories

    print(all_repositories)

    return []







    # Get relationships between repositories and their owners    
    # Get the relationships between users and their owned repositories





def find_close_items(db: SupabaseNetworkDatabase, item_id, item_type):

    most_similar_nodes = get_most_similar_nodes(
        get_all_nodes(db),
        get_all_relationships(db), 
        item_id,
        item_type,
    )

    return most_similar_nodes




def network_test():


    find_close_items("1", "user")