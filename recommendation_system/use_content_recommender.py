import typing as t
from sample_data import sample_repositories, sample_users, sample_relationships
from sentence_transformers import SentenceTransformer
from content_recommender import RecommendableItem, ContentRecommender, GeneralContentDatabase




class User(RecommendableItem):
    def __init__(self, user_data: object):
        self.id = user_data["id"]
        self.description = user_data.get("description") or ""
        self.interest = user_data.get("interest") or ""
        self.skills = user_data.get("skills") or ""
        self.availability = user_data.get("availability") or ""

        text = " ".join([self.description, self.interest, self.skills])

        super().__init__(self.id, text, "user")


    def __repr__(self):
        return f"User {self.id} with description \"{self.description}\""



class Repository(RecommendableItem):
    def __init__(self, repo_data: object):
        self.id = repo_data["id"]
        self.description = repo_data.get("description") or ""
        self.languages = repo_data.get("languages") or ""
        
        text = " ".join([self.description, self.languages])

        super().__init__(self.id, text, "repository")


    def __repr__(self):
        return f"Repository {self.id} with description \"{self.description}\""



def recommend_repos_for_user(user_id: str, db: GeneralContentDatabase,
                             user_features: t.List[str] = ["description", "interest", "skills"],
                             repo_features: t.List[str] = ["description", "languages"]):


def recommend_users_for_repo(repository_id: str, db: GeneralContentDatabase,
                             user_features: t.List[str] = ["description", "interest", "skills"],
                             repo_features: t.List[str] = ["description", "languages"]):
    repository = db.get_item("repository", repository_id)
    return ContentRecommender(db).recommend_items_for_item(repository, "user", repo_features, user_features)




def content_test():
    
    db = ()

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # sss = SemanticSimilaritySearch(model)

    # desc = pd.DataFrame(repositories).set_index("id").loc["repository5"]["description"]
    # words = sss.remove_stopwords(desc)
    # keywords = sss.extract_keywords(desc)
    # print(keywords)

    print(recommend_users_for_repo("5", db))

    print(recommend_repos_for_user("3", db))


