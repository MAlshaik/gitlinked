from sample_data import repositories, users, relationships
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.description = data["description"]
        self.skills = data["skills"]
        

    def embed_description(self, model: SentenceTransformer):
        embedding = model.encode(self.description+" "+self.skills)
        # save embedding to database
        return embedding
    

    def get(user_id):
        user_data = [i for i in users if i["id"] == user_id][0]
        return User(user_data)
    

    def get_repository_matches(self, model: SentenceTransformer):
        user = User.get(self.id)
        user_embedding = user.embed_description(model)

        all_repositories = [Repository.get(i["id"]) for i in repositories]

        repository_embeddings = pd.DataFrame([i.embed_description(model) for i in all_repositories], index=[i.id for i in all_repositories])

        user_to_repo_similarity = cosine_similarity([user_embedding], repository_embeddings)
        
        # return a dataframe of repository ids and their similarity to the user
        return pd.DataFrame(user_to_repo_similarity, columns=repository_embeddings.index.tolist(), index=[self.id])






class Repository:
    def __init__(self, data):
        self.id = data["id"]
        self.description = data["description"]
        self.languages = data["languages"]

    def get(repository_id):
        repository_data = [i for i in repositories if i["id"] == repository_id][0]
        return Repository(repository_data)


    def embed_description(self, model: SentenceTransformer):
        embedding = model.encode(self.description+" "+self.languages)
        # save embedding to database
        return embedding
    
    def get_user_matches(self, model: SentenceTransformer):
        repository = Repository.get(self.id)
        repository_embedding = repository.embed_description(model)

        all_users = [User.get(i["id"]) for i in users]

        user_embeddings = pd.DataFrame([i.embed_description(model) for i in all_users], index=[i.id for i in all_users])

        # print(user_embeddings)
        repo_to_users_similarity = cosine_similarity([repository_embedding], user_embeddings)

        # return a dataframe of user ids and their similarity to the repository
        return pd.DataFrame(repo_to_users_similarity, columns=user_embeddings.index.tolist(), index=[self.id])




class TextParser:

    def __init__(self, model: SentenceTransformer):
        self.model = model


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

    model = SentenceTransformer('all-MiniLM-L6-v2')

    if (repository_id):
        return Repository.get(repository_id).get_user_matches(model)
    
    elif (user_id):
        return User.get(user_id).get_repository_matches(model)




if __name__ == "__main__":

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # sss = SemanticSimilaritySearch(model)

    # desc = pd.DataFrame(repositories).set_index("id").loc["repository5"]["description"]
    # words = sss.remove_stopwords(desc)
    # keywords = sss.extract_keywords(desc)
    # print(keywords)

    print(get_recommendations_by_desc(repository_id="repository5"))
    print(get_recommendations_by_desc(user_id="user3"))

