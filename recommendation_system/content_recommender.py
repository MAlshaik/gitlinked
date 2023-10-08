from sentence_transformers import SentenceTransformer


class RecommendationDatabase:
    def __init__(self):
        pass



class RecommendableItem:
    def __init__(self, id: int, text: str, type: str):
        self.id = id
        self.text = text
        self.type = type


class ContentRecommender:
    def embed_item_text(self, item: RecommendableItem):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embedding = model.encode(item.text)
        return embedding




