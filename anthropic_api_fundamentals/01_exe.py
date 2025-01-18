from dotenv import load_dotenv
import os

load_dotenv()
# my_api_key = os.getenv("ANTHROPIC_API_KEY")

from anthropic import Anthropic

# client = Anthropic(api_key=my_api_key)
# automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hi there! Please tell me a joke"},
    ],
)

print(first_message.content[0])
