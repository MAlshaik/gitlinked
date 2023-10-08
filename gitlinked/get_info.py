import requests
import base64
import json
import argparse
import dotenv
import os
from helper import getUserInfo


dotenv.load_dotenv()
git_token=os.getenv("GITHUB_TOKEN")


parser = argparse.ArgumentParser(description='Enter user id.')
parser.add_argument('--username', metavar='N', type=str,
                    help='github username')
parser.add_argument('--id', metavar='N', type=str,
                    help='github id')
parser.add_argument('--exists', metavar='N', type=str, default=False,
                    help='does the entry aready exist in the database')
                    
args = parser.parse_args()
id_ = args.id
exists = args.exists
repos_data = getUserInfo(args.username)
    

# Open a file named 'output.json' for writing
body = {'exists': exists,
        'id': id_,
        'repos': repos_data,
        'interest': ' ',
        'availibility': 0,
        'skills': []}

our_api_url = 'http://localhost:3000/api/addUserRepoDetails'

response = requests.post(url=our_api_url, json=body)
print(response)