import pandas as pd
from node2vec import Node2Vec
import networkx as nx
from sample_data import sample_users, sample_repositories, sample_relationships
from database import Database
import typing



def get_network_relationships(db: Database):
    all_users = db.get_users()
    all_repositories = db.get_repositories()



def create_graph(relationships: typing.List[tuple[str, str]], user_ids, repository_ids, tag_ids=[]):
    G = nx.Graph()
    for user_id in user_ids:
        G.add_node("user-"+user_id["id"])
    for repository_id in repository_ids:
        G.add_node("repository-"+repository_id["id"])
    for tag_id in tag_ids:
        G.add_node("tag-"+tag_id["id"])
    for relationship in relationships:
        G.add_edge(*[i[0]+"-"+i[1] for i in relationship])

    return G


if __name__ == "__main__":
    G = create_graph(sample_relationships, sample_users, sample_repositories)
    n2v = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = n2v.fit(window=10, min_count=1, batch_words=4)

    # return a dataframe of repositories

    print(model.wv.most_similar("user-1"))


