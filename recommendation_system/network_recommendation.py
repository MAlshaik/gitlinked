import pandas as pd
from node2vec import Node2Vec
import networkx as nx
from sample_data import sample_users, sample_repositories, sample_relationships
import typing






def create_graph(relationships: typing.List[tuple[str, str]], users, repositories, tags=[]):
    G = nx.Graph()
    for user in users:
        G.add_node("user-"+user["id"])
    for repository in repositories:
        G.add_node("repository-"+repository["id"])
    for tag in tags:
        G.add_node("tag-"+tag["id"])
    for relationship in relationships:
        G.add_edge(*[i[0]+"-"+i[1] for i in relationship])

    print(G.nodes(data=True))

    return G


if __name__ == "__main__":
    G = create_graph(sample_relationships, sample_users, sample_repositories)
    n2v = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    # return a dataframe of repositories

    print(model.wv.most_similar("user-1"))







