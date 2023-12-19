import openai
import os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

if not api_key:
    raise ValueError("OpenAI API key not found. Make sure it's set in the .env file.")
Text_input = input("Enter Text:")
response_variables = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    format="text",
    messages=[
        {"role": "system",
        "content": "You are a helpful assistant that can extract values from text. every word is a common noun, don't consider anything as proper noun"},
        {"role": "user", "content": Text_input},
    ]
)

extracted_json = response_variables.choices[0].message.content

print(extracted_json)