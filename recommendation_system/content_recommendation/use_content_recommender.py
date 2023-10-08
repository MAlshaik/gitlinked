from sample_data import sample_repositories, sample_users, sample_relationships
from sentence_transformers import SentenceTransformer
from content_recommender import RecommendableItem, ContentRecommender, ContentDatabase




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






class TestDatabase(ContentDatabase):

    def __init__(self):
        pass


    def get_user(self, user_id):
        return [i for i in sample_users if i["id"] == user_id][0]


    def get_repository(self, repository_id):
        return [i for i in sample_repositories if i["id"] == repository_id][0]


    def get_users(self):
        return [User(i) for i in sample_users]


    def get_repositories(self):
        return [Repository(i) for i in sample_repositories]


    def save_user_description_embedding(self, user_id, embedding):
        pass


    def save_repository_description_embedding(self, repository_id, embedding):
        pass



def recommend_repos_for_user(user_id: str, db: ContentDatabase, prompt_keywords: str = None):

    user = User(db.get_item("user", user_id))
    
    if prompt_keywords:
        user.text = user.text + " " + prompt_keywords

    return ContentRecommender(db).recommend_items_for_item(user, "repository")


def recommend_users_for_repo(repository: Repository, db: ContentDatabase):
    return ContentRecommender(db).recommend_items_for_item(repository, "user")



class ContentBasedRecommendation:

    def __init__(self, model: SentenceTransformer, database: TestDatabase):
        self._model = model
        self._db = database



def test():
    
    db = TestDatabase()

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # sss = SemanticSimilaritySearch(model)

    # desc = pd.DataFrame(repositories).set_index("id").loc["repository5"]["description"]
    # words = sss.remove_stopwords(desc)
    # keywords = sss.extract_keywords(desc)
    # print(keywords)

    print(recommend_users_for_repo(Repository(db.get_repository("5")), db))
    print(recommend_repos_for_user(User(db.get_user("3")), db))

