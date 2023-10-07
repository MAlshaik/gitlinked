import requests
import base64
import json
import argparse



parser = argparse.ArgumentParser(description='Enter user id.')
parser.add_argument('--username', metavar='N', type=str,
                    help='github username')
parser.add_argument('--id', metavar='N', type=str,
                    help='github username')
                    
args = parser.parse_args()
id_ = args.id
# Your personal access token
token = input("Enter your GitHub token: ")

# Set up the headers for your requests, including your token for authorization
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

github_username = args.username  # specify your User name

# api url to grab public user repositories
api_url = f"https://api.github.com/users/{github_username}/repos"

# send get request
response = requests.get(api_url, headers=headers)

# get the json data
data = response.json()

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
    

# Open a file named 'output.json' for writing
print(repos_data)
body = {'id': id_,
        'repos': repos_data,
        'interest': ' ',
        'availibility': 0,
        'skills': []}

our_api_url = 'http://localhost:3000/api/addUserRepoDetails'

response = requests.post(url=our_api_url, json=body)
print(response)