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

repo_name = "chrislgarry/Apollo-11"
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


# Organize data
output_data = {
    "Repository": owner + "/" + repo,
    "Languages": languages_data,
    "Description": repo_data.get("description", ""),
    "README": readme_content,
    "Contributors": contributors_data
}

# Write to output.json
with open('output2.json', 'w') as f:
    json.dump(output_data, f, indent=4)
