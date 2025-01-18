from dotenv import load_dotenv
import os

load_dotenv()
# my_api_key = os.getenv("ANTHROPIC_API_KEY")

from anthropic import Anthropic
import sys

# client = Anthropic(api_key=my_api_key)
# automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()


if len(sys.argv) != 3:
    print("Usage: python script.py 'text' language")
    sys.exit(1)

txt = sys.argv[1]
lang = sys.argv[2]


def translate(text, language):
    res = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        system=f"Please translate the text defined by the user to {language}. Important: Return only the translated text.",
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return res.content[0].text


print(translate(txt, lang))
