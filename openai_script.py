import openai

# Set your API key
openai.api_key = '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'


def extract_info(text):
    # Define a system message to instruct the assistant
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant that extracts information regarding interests, skills, and time commitment from a given text.\
        The dafault for interests is Astronomy, the default for skills is Python, the default for time commitment is 2 hours per week.\
        Use the default information if you cannot find information to extract.\
        Return all the interests, skills, and time commitment as a comma-separated list of strings."
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
text_input = "i am interested in machine learning and neuroscience, i have experience in nlp and web design, i can work 5 hours per week."
assistant_reply = extract_info(text_input)
print(assistant_reply)
