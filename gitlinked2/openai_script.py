import openai
import dotenv
import requests
import os
import argparse
dotenv.load_dotenv()

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("NEXTAUTH_URL")

parser = argparse.ArgumentParser(description='Enter user id.')
parser.add_argument('--id', metavar='N', type=str,
                    help='github username')
parser.add_argument('--prompt', type=str)
args = parser.parse_args()

def extract_info(text):
    # Define a system message to instruct the assistant
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant that extracts information regarding interests, skills, and time commitment from a given text.\
        The dafault for interests is Astronomy, the default for skills is Python, the default for time commitment is 2 hours per week.\
        Use the default information if you cannot find information to extract.\
        Return all the interests, skills, and time commitment(int) as a comma-separated list of strings. But each of the values(interest, skill, time commitment) are separated by semicolons"
    }

    # Define a user message with the text input
    user_message = {
        "role": "user",
        "content": text
    }

    # Send a request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message]
    )

    # Extracting assistant's reply
    assistant_reply = response['choices'][0]['message']['content']

    return assistant_reply


# Example usage
#text_input = "i am interested in machine learning and neuroscience, i have experience in nlp and web design, i can work 5 hours per week."
assistant_reply = extract_info(args.prompt)
#print(assistant_reply)

interests = assistant_reply.split(';')[0]
skills = assistant_reply.split(';')[1]
time_commitment = int(assistant_reply.split(';')[2])

body_interest = {"interest" : interests, "id": int(args.id)}
skills_body = {"skills" : skills, "id" : int(args.id)}
time_commitment_body = {"availibility" : time_commitment, "id" : int(args.id)}

response_interest = requests.post(
    url=BASE_URL+'api/updateInterest', json=body_interest)
response_skills = requests.post(
    url=BASE_URL+'api/updateSkills', json=skills_body)
availibility_response = requests.post(
    url=BASE_URL+'api/updateAvailibility', json=time_commitment_body
)

