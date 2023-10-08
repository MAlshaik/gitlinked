import requests
from prettytable import PrettyTable

# Your personal access token
token = input("Enter your GitHub token: ")

# Set up the headers for your requests, including your token for authorization
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

# Specify the User ID
user_id = 3440094  # replace with the actual user ID

# API URL to grab user information by ID
api_url = f"https://api.github.com/user/{user_id}"

# Send GET request
response = requests.get(api_url, headers=headers)

# Get the JSON data
data = response.json()

# Print the username
print(data.get('login', 'Username not found'))
