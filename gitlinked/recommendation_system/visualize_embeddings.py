

def visualize(embeddings):

    transform = TSNE  # or PCA
    node_embeddings_2d = transform(n_components=2).fit_transform(node_embeddings)