import typing as t
from network_recommender import get_most_similar_nodes, GraphNode, GraphRelationship
from network_database import SupabaseNetworkDatabase
import enum
import pandas as pd



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





def find_close_items(db: SupabaseNetworkDatabase, item_id, item_type, top_n=10) -> t.Tuple[pd.DataFrame, pd.DataFrame]:

    most_similar_nodes = get_most_similar_nodes(
        get_all_nodes(db),
        get_all_relationships(db), 
        item_id,
        item_type,
    )

    df = pd.DataFrame([GraphNode.id_to_type_and_item_id(i[0]) + list(i)[1:] for i in most_similar_nodes],
        columns=["type", "id", "similarity"]).sort_values(by="similarity", ascending=False)

    # split the dataframe into two, based on type
    df_users = df[df["type"] == NodeType.USER.value]
    df_repositories = df[df["type"] == NodeType.REPOSITORY.value]

    # return the first n columns of each dataframe

    return df_users.head(top_n), df_repositories.head(top_n)

