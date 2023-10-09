from sentence_transformers import SentenceTransformer
import typing as t
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import nltk
from supabase_base import SupabaseDatabase




class RecommendableItem:
    def __init__(self, id: int, text: str, type: str):
        self.id = id
        self.text = text
        self.type = type


class GeneralContentDatabase(SupabaseDatabase):
    def __init__(self):
        super().__init__()


    def get_all_items(self, type: str) -> t.List[RecommendableItem]:
        pass

    def get_item(self, type: str, item_id: str) -> RecommendableItem:
        pass



class ContentRecommender:

    def __init__(self, database: GeneralContentDatabase):
        self.db = database
        self.model = SentenceTransformer('all-MiniLM-L6-v2')


    def embed_item_text(self, item: RecommendableItem, features_to_use: t.List[str] = ["text"]):
        # uses tfidf to extract keywords from a list of words

        text = " ".join([getattr(item, i) for i in features_to_use])

        filtered_text = self.remove_stopwords(text)
        
        nltk.download('punkt')
        nltk.download('stopwords')
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')

        all_items = self.db.get_all_items(item.type)
        all_texts = [i.text for i in all_items]
        print(all_texts)

        keyword_text = " ".join(filtered_text)
        embedding = self.model.encode(keyword_text)

        return embedding
    


    def recommend_items_for_item(self, item: RecommendableItem, type_to_recommend: str, 
                                 features_of_item: t.List[str] = ["text"],
                                 features_of_type_to_recommend: t.List[str] = ["text"]):

        item_embedding =  self.embed_item_text(item, features_of_item)
        all_other_items = self.db.get_all_items(type_to_recommend)

        print("ALL OTHER ITEMS", all_other_items)

        other_item_embeddings = pd.DataFrame([self.embed_item_text(i, features_of_type_to_recommend) for i in all_other_items], index=[i.id for i in all_other_items])
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






