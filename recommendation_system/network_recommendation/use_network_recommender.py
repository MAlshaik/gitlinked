import typing as t
from network_recommender import get_most_similar_nodes, GraphNode
from network_database import SupabaseNetworkDatabase
import enum



class NodeType(enum.Enum):
    USER = "user"
    REPOSITORY = "repository"
    TAG = "tag"



def _generate_graph_nodes(
    all_user_ids: t.List[str], 
    all_repository_ids: t.List[str],
    all_tag_ids: t.List[str]=[]
):

    all_users = [GraphNode(i, NodeType.USER) 
                 for i in all_user_ids]

    all_repositories = [GraphNode(i, NodeType.REPOSITORY) 
                        for i in all_repository_ids]
    
    all_tags = [GraphNode(i, NodeType.TAG)
                for i in all_tag_ids]

    return all_users + all_repositories + all_tags



def run(item_id, item_type):

    db = SupabaseNetworkDatabase()


    all_nodes = _generate_graph_nodes(
        db.get_all_user_ids(),
        db.get_all_repository_ids(),
        db.get_all_tag_ids()
    )

    most_similar_nodes = get_most_similar_nodes(
        db.get_all_relationships(),
        all_nodes,
        item_id,
        item_type
    )

    return most_similar_nodes




def test():


    run("1", "user")