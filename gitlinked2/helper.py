import requests
import dotenv
import os
import base64
import json

dotenv.load_dotenv()


def getUserInfo(github_username):
    api_url = f"https://api.github.com/users/{github_username}/repos"
    git_token=os.getenv("GITHUB_TOKEN")
    print(git_token)

    headers = {
        "Authorization": f"token {git_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    # send get request
    print(headers)
    response = requests.get(api_url, headers=headers)

    # get the json data
    data = response.json()
    print(data)

    # Create an empty list to hold the repository data
    repos_data = {}
    for n, repository in enumerate(data):
        
        repository_name = repository["name"]
        repository_description = repository["description"]
        if not repository_description:
            repository_description = ""

        languages_url = f"https://api.github.com/repos/{github_username}/{repository_name}/languages"
        languages_response = requests.get(languages_url, headers=headers)
        languages_data = languages_response.json()
        temp = ""
        for lang in languages_data:
            temp += lang + ", "
        languages_data = temp

        readme_url = f"https://api.github.com/repos/{github_username}/{repository_name}/readme"
        readme_response = requests.get(readme_url, headers=headers)
        readme_data = readme_response.json()
        if 'content' in readme_data:
            # Decode the Base64 encoded README content
            readme_content = base64.b64decode(
                readme_data['content']).decode('utf-8')
        else:
            readme_content = ""
        
        repos_data[n] = {
            "Repository": repository_name,
            "Languages": languages_data,
            "Description": repository_description,
            "README": readme_content
        }
        
    return repos_data

