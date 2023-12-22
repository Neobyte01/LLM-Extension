import os
from dotenv import load_dotenv
from openai import OpenAI



# API key and client configuration
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key= api_key
)



# Function to get a response from the OpenAI chatbot
def get_response(massage, rule): 

    # Create a chat completion request using the OpenAI API
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": rule
        },
        {
        "role": "user",
        "content": massage
        }
    ],
    stream=True,
    temperature=0.7,
    max_tokens=64,
    top_p=1
    )

    # return the response
    output = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            output += chunk.choices[0].delta.content
    return output



# example
response = get_response("how are are and what are you doint?", "rewrite this qusetion")
print(response)

