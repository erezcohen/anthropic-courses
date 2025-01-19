from dotenv import load_dotenv
from anthropic import Anthropic
import sys
import os

load_dotenv()

client = Anthropic()

history = []


def callModel():
    res = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=history,
    )
    return res.content[0].text


def flow():
    while True:
        txt = input("Enter text: ")
        if txt == "exit":
            break
        history.append({"role": "user", "content": txt})
        res = callModel()
        print(res)
        history.append({"role": "assistant", "content": res})


flow()
