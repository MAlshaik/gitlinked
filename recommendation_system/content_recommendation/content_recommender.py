from sentence_transformers import SentenceTransformer
import typing as t
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')




class RecommendableItem:
    def __init__(self, id: int, text: str, type: str):
        self.id = id
        self.text = text
        self.type = type


class ContentDatabase:
    def __init__(self):
        pass

    def get_all_items(self, type: str) -> t.List[RecommendableItem]:
        pass

    def get_item(self, type: str, item_id: str) -> RecommendableItem:
        pass



class ContentRecommender:

    def __init__(self, database: ContentDatabase):
        self.db = database



    def embed_item_text(self, item: RecommendableItem):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embedding = model.encode(item.text)
        return embedding
    


    def recommend_items_for_item(self, item: RecommendableItem, type_to_recommend: str):

        item_embedding =  self.embed_item_text(item)
        all_other_items = self.db.get_all_items(type_to_recommend)
        other_item_embeddings = pd.DataFrame([self.embed_item_text(i) for i in all_other_items], index=[i.id for i in all_other_items])
        similarities = cosine_similarity([item_embedding], other_item_embeddings)
        
        # return a dataframe with one column where rows are each other item and it's associated score
        return pd.DataFrame(similarities.T, index=other_item_embeddings.index, columns=["match_score"]).sort_values("match_score", ascending=False)



    def remove_stopwords(self, text):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        return filtered_sentence
    

    def extract_keywords(self, text: str):
        # uses tfidf to extract keywords from a list of words
        
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        documents = pd.DataFrame()



