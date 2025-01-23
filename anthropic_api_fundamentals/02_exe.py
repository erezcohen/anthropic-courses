from dotenv import load_dotenv
import os
from typing import Optional
from anthropic import Anthropic
import sys

load_dotenv()
# my_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")

# client = Anthropic(api_key=my_api_key)
# automatically looks for an "ANTHROPIC_API_KEY" environment variable
client: Anthropic = Anthropic()

if len(sys.argv) != 3:
    print("Usage: python script.py 'text' language")
    sys.exit(1)

txt: str = sys.argv[1]
lang: str = sys.argv[2]


def translate(text: str, language: str) -> str:
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
