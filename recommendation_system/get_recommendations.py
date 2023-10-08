from sample_data import sample_repositories, sample_users, sample_relationships
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from content_recommender import RecommendableItem, ContentRecommender

nltk.download('punkt')
nltk.download('stopwords')


class Database:

    def __init__(self):
        pass

    def get_user(self, user_id):
        return [i for i in sample_users if i["id"] == user_id][0]

    def save_user_description_embedding(self, user_id, embedding):
        pass
    
    def get_repository(self, repository_id):
        return [i for i in sample_repositories if i["id"] == repository_id][0]
    
    def save_repository_description_embedding(self, repository_id, embedding):
        pass
    
    def get_users(self):
        return [User(i) for i in sample_users]
    
    def get_repositories(self):
        return [Repository(i) for i in sample_repositories]



class User(RecommendableItem):
    def __init__(self, user_data: object):
        self.id = user_data["id"]
        self.description = user_data["description"]
        self.skills = user_data.get("skills") or ""

        text = self.description + " " + self.skills

        super().__init__(self.id, text, "user")



class Repository(RecommendableItem):
    def __init__(self, repo_data: object):
        self.id = repo_data["id"]
        self.description = repo_data["description"]
        self.languages = repo_data["Languages"]
        
        text = self.description+" "+(self.languages or "")

        super().__init__(self.id, text, "repository")



def recommend_repos_for_user(user: User, db: Database):
    user_embedding =  ContentRecommender().embed_item_text(user)
    all_repositories = db.get_repositories()
    repository_embeddings = pd.DataFrame([ContentRecommender().embed_item_text(i) for i in all_repositories], index=[i.id for i in all_repositories])
    user_to_repo_similarity = cosine_similarity([user_embedding], repository_embeddings)
    
    # return a dataframe with one column where rows are each repository and it's associated score
    return pd.DataFrame(user_to_repo_similarity.T, index=repository_embeddings.index, columns=["match_score"]).sort_values("match_score", ascending=False)



def recommend_users_for_repo(repository: Repository, db: Database):
    repository_embedding = ContentRecommender().embed_item_text(repository)
    all_users = db.get_users()
    user_embeddings = pd.DataFrame([ContentRecommender().embed_item_text(i) for i in all_users], index=[i.id for i in all_users])
    repo_to_users_similarity = cosine_similarity([repository_embedding], user_embeddings)

    # return a dataframe  with one column where rows are each user and it's associated score
    return pd.DataFrame(repo_to_users_similarity.T, index=user_embeddings.index, columns=["match_score"]).sort_values("match_score", ascending=False)



class ContentBasedRecommendation:

    def __init__(self, model: SentenceTransformer, database: Database):
        self._model = model
        self._db = database


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
        documents = pd.DataFrame(self._db.get_repositories())
        
        



if __name__ == "__main__":
    
    db = Database()

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # sss = SemanticSimilaritySearch(model)

    # desc = pd.DataFrame(repositories).set_index("id").loc["repository5"]["description"]
    # words = sss.remove_stopwords(desc)
    # keywords = sss.extract_keywords(desc)
    # print(keywords)

    print(recommend_users_for_repo(Repository(db.get_repository("5")), db))
    print(recommend_repos_for_user(User(db.get_user("3")), db))

