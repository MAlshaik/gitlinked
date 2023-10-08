from sample_data import sample_repositories, sample_users, sample_relationships
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
        return sample_users
    
    def get_repositories(self):
        return sample_repositories





class User:
    def __init__(self, user_data: object, db: Database):
        print("user_data", user_data)
        self.id = user_data["id"]
        self.description = user_data["description"]
        self.skills = user_data["skills"]

        self.db = db


    def get_repository_matches(self):
        user_embedding =  embed_user_text(self, self.db)

        all_repositories = self.db.get_repositories()

        repository_embeddings = pd.DataFrame([embed_repository_text(i, self.db) for i in all_repositories], index=[i.id for i in all_repositories])

        user_to_repo_similarity = cosine_similarity([user_embedding], repository_embeddings)
        
        # return a dataframe with one column where rows are each repository and it's associated score
        return pd.DataFrame(user_to_repo_similarity.T, index=repository_embeddings.index, columns=["match_score"]).sort_values("match_score", ascending=False)



    def get_description(self):
        return self.description+" "+self.skills



class Repository:
    def __init__(self, repo_data: object, db: Database):
        print(repo_data)
        self.id = repo_data["id"]
        self.description = repo_data["description"]
        self.languages = repo_data["Languages"]

        self.db = db


    def get_user_matches(self):
        repository_embedding = embed_repository_text(self, self.db)

        all_users = self.db.get_users()

        user_embeddings = pd.DataFrame([embed_user_text(i, self.db) for i in all_users], index=[i.id for i in all_users])

        repo_to_users_similarity = cosine_similarity([repository_embedding], user_embeddings)

        # return a dataframe  with one column where rows are each user and it's associated score
        return pd.DataFrame(repo_to_users_similarity.T, index=user_embeddings.index, columns=["match_score"]).sort_values("match_score", ascending=False)

    def get_description(self):
        return self.description+" "+(self.languages or "")



def embed_user_text(user: User, db: Database):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    embedding = model.encode(user.get_description())
    db.save_user_description_embedding(user.id, embedding)
    return embedding


def embed_repository_text(repository: Repository, db: Database):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(repository.get_description())
    db.save_repository_description_embedding(repository.id, embedding)
    return embedding





class TextParser:

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

    print(Repository(db.get_repository("repository5"), db).get_user_matches())
    print(User(db.get_user("user3"), db).get_repository_matches())

