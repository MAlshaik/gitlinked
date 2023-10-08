import typing as t
from node2vec import Node2Vec
import networkx as nx
import sys, os



class GraphNode:
    def __init__(self, item_id: str, item_type: str):
        self.item_id = item_id
        self.type = item_type

        self.id = self.type + " " + self.item_id

    def id_to_type_and_item_id(id: str) -> t.List[str]:
        # returns a list of [type, id] from the id string
        return id.split(" ")


    def __repr__(self):
        return f"GraphNode({self.item_id}, {self.type})"



class GraphRelationship:
    def __init__(self, node1: GraphNode, node2: GraphNode):
        self.node1_id = node1.item_id
        self.node2_id = node2.item_id




def _train_embedding_model(all_relationships: t.List[GraphRelationship], all_nodes: t.List[GraphNode]):

    print(all_nodes)

    G = nx.Graph()
    for node in all_nodes:
        G.add_node(node.id)
    for relationship in all_relationships:
        G.add_edge(relationship.node1_id, relationship.node2_id)

    print(G.nodes)

    n2v = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    return model




def get_most_similar_nodes(all_nodes: t.List[GraphNode], all_relationships: t.List[GraphRelationship], item_id: str, item_type: str, topn=10):

    model = _train_embedding_model(all_relationships, all_nodes)

    node_id = GraphNode(item_id, item_type).id

    return model.wv.most_similar(node_id, topn=topn)
    







