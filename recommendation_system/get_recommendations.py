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
    def __init__(self, user_data, db: Database):
        self.id = user_data["id"]
        self.description = user_data["description"]
        self.skills = user_data["skills"]

        self.db = db

        self._model = SentenceTransformer('all-MiniLM-L6-v2')
        

    def embed_description(self):
        embedding = self._model.encode(self.description+" "+self.skills)
        # save embedding to database
        return embedding


    def get_repository_matches(self):
        user_embedding = self.embed_description()

        all_repositories = [Repository(i, self.db) for i in self.db.get_repositories()]

        repository_embeddings = pd.DataFrame([i.embed_description() for i in all_repositories], index=[i.id for i in all_repositories])

        user_to_repo_similarity = cosine_similarity([user_embedding], repository_embeddings)
        
        # return a dataframe of repository ids and their similarity to the user
        return pd.DataFrame(user_to_repo_similarity, columns=repository_embeddings.index.tolist(), index=[self.id])





class Repository:
    def __init__(self, repo_data, db: Database):
        self.id = repo_data["id"]
        self.description = repo_data["description"]
        self.languages = repo_data["languages"]

        self.db = db

        self._model = SentenceTransformer('all-MiniLM-L6-v2')

    # def get(repository_id):
    #     repository_data = self.db.get_repository(repository_id)
    #     return Repository(repository_data)


    def embed_description(self):
        embedding = self._model.encode(self.description+" "+self.languages)
        # save embedding to database
        return embedding
    
    def get_user_matches(self):
        repository_embedding = self.embed_description()

        all_users = [User(i, self.db) for i in self.db.get_users()]

        user_embeddings = pd.DataFrame([i.embed_description() for i in all_users], index=[i.id for i in all_users])

        # print(user_embeddings)
        repo_to_users_similarity = cosine_similarity([repository_embedding], user_embeddings)

        # return a dataframe of user ids and their similarity to the repository
        return pd.DataFrame(repo_to_users_similarity, columns=user_embeddings.index.tolist(), index=[self.id])




class TextParser:

    def __init__(self, model: SentenceTransformer):
        self._model = model


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
        tfidf_matrix = tfidf_vectorizer.fit_transform([text])
        feature_names = tfidf_vectorizer.get_feature_names_out()
        print(feature_names)
        dense = tfidf_matrix.todense()
        denselist = dense.tolist()
        df = pd.DataFrame(denselist, columns=feature_names)
        df = df.transpose()
        df = df.sort_values(by=0, ascending=False)
        df = df[df[0] > 0]
        return df.index.tolist()
        
        


def get_recommendations_by_desc(user_id=None, repository_id=None):

    db = Database()

    if (repository_id):
        return Repository(db.get_repository(repository_id), db).get_user_matches()
    
    elif (user_id):
        return User(db.get_user(user_id), db).get_repository_matches()




if __name__ == "__main__":

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # sss = SemanticSimilaritySearch(model)

    # desc = pd.DataFrame(repositories).set_index("id").loc["repository5"]["description"]
    # words = sss.remove_stopwords(desc)
    # keywords = sss.extract_keywords(desc)
    # print(keywords)

    print(get_recommendations_by_desc(repository_id="repository5"))
    print(get_recommendations_by_desc(user_id="user3"))

