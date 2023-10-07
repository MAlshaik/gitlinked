import requests
from prettytable import PrettyTable

# Your personal access token
token = input("Enter your GitHub token: ")

# Set up the headers for your requests, including your token for authorization
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

table = PrettyTable()
table.field_names = ["Repository Name", "Description"]

github_username = "Uzairname"  # specify your User name

# api url to grab public user repositories
api_url = f"https://api.github.com/users/{github_username}/repos"

# send get request
response = requests.get(api_url, headers=headers)

# get the json data
data = response.json()

for repository in data:
    repository_name = repository["name"]
    languages_url = f"https://api.github.com/repos/{github_username}/{repository_name}/languages"
    languages_response = requests.get(languages_url, headers=headers)
    languages_data = languages_response.json()
    print(languages_data)

for repository in data:
    table.add_row([repository["name"], repository["description"]])

print(table)
