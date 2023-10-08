import pandas as pd
from node2vec import Node2Vec
import networkx as nx
from sample_data import sample_users, sample_repositories, sample_relationships
from database import Database
import typing
import enum




class GraphNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

class GraphRelationship:
    def __init__(self, node1: GraphNode, node2: GraphNode):
        self.node1_id = node1.node_id
        self.node2_id = node2.node_id


def create_graph(
        relationships: typing.List[GraphRelationship],
        nodes: typing.List[GraphNode]
):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node.node_id)
    for relationship in relationships:
        G.add_edge(relationship.node1_id, relationship.node2_id)

    return G



class NodeType(enum.Enum):
    USER = "user"
    REPOSITORY = "repository"
    TAG = "tag"


def get_network_relationships(db: Database):
    all_users = [GraphNode(NodeType.USER + i["id"], NodeType.USER) 
                 for i in db.get_users()]

    all_repositories = [GraphNode(NodeType.REPOSITORY + i["id"], NodeType.REPOSITORY) 
                        for i in db.get_repositories()]


if __name__ == "__main__":
    G = create_graph(sample_relationships, sample_users, sample_repositories)
    n2v = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    # return a dataframe of repositories

    print(model.wv.most_similar("user-1"))





