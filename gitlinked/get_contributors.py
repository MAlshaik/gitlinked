import requests
import base64
import json
import dotenv
import os
import argparse
from helper import getUserInfo 

dotenv.load_dotenv()
git_token=os.getenv("GITHUB_TOKEN")

# Your personal access token

# Set up the headers for your requests, including your token for authorization
headers = {
    "Authorization": f"token {git_token}",
    "Accept": "application/vnd.github.v3+json",
}
parser = argparse.ArgumentParser(description='Enter user id.')
parser.add_argument('--name', metavar='N', type=str,
                    help='github username')
                    
args = parser.parse_args()
repo_name = args.name
owner, repo = repo_name.split('/')

# Gather repository, languages, and README data
repo_url = f"https://api.github.com/repos/{repo_name}"
repo_response = requests.get(repo_url, headers=headers)
repo_data = repo_response.json()

languages_url = f"https://api.github.com/repos/{repo_name}/languages"
languages_response = requests.get(languages_url, headers=headers)
languages_data = ', '.join(languages_response.json().keys())

readme_url = f"https://api.github.com/repos/{repo_name}/readme"
readme_response = requests.get(readme_url, headers=headers)
readme_data = readme_response.json()
readme_content = base64.b64decode(readme_data['content']).decode(
    'utf-8') if 'content' in readme_data else ""

# Gather contributors data
contributors_url = f"https://api.github.com/repos/{repo_name}/contributors"
contributors_response = requests.get(contributors_url, headers=headers)
contributors_data = [(item["login"], item["id"])
                     for item in contributors_response.json()]
url_add_user = 'http://localhost:3000/api/addUser'
for user in contributors_data:
    
    data = getUserInfo(user[0])
    body = {
        "username" : user[0],
        "id" : user[1],
        "repos" : data

    }
    response = requests.post(url_add_user, json=body)
    print('Added user or not')
# Organize data
output_data = {
    "repo_name": owner + "/" + repo,
    "languages": languages_data,
    "description": repo_data['description'],
    "README": readme_content,
    "top_contributors": contributors_data
}


url = 'http://localhost:3000/api/addRepo'
response = requests.post(url=url, json=output_data)
print(response)

