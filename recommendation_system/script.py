import pandas as pd
from node2vec import Node2Vec
import networkx as nx
from sample_data import users, repositories, relationships



def create_graph(users, repositories, relationships):
    G = nx.Graph()
    for user in users:
        G.add_node(user["id"])
    for repository in repositories:
        G.add_node(repository["id"])
    for relationship in relationships:
        G.add_edge(*relationship)

    print(G.nodes(data=True))

    return G


if __name__ == "__main__":
    G = create_graph(users, repositories, relationships)
    n2v = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    print(model.wv.most_similar("user1"))












