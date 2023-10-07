import requests
import base64
import json

# Your personal access token
token = input("Enter your GitHub token: ")

# Set up the headers for your requests, including your token for authorization
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

github_username = "uzairname"  # specify your User name

# api url to grab public user repositories
api_url = f"https://api.github.com/users/{github_username}/repos"

# send get request
response = requests.get(api_url, headers=headers)

# get the json data
data = response.json()

# Create an empty list to hold the repository data
repos_data = []

for repository in data:
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

    repos_data.append({
        "Repository": repository_name,
        "Languages": languages_data,
        "Description": repository_description,
        "README": readme_content
    })

# Open a file named 'output.json' for writing
with open('output.json', 'w') as f:
    json.dump(repos_data, f, indent=4)
