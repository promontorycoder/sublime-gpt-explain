#!/usr/bin/env python3

import os
import sys
from openai import OpenAI

# Setup client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read the code from stdin
code = sys.stdin.read()

# Get optional language hint from environment
lang_hint = os.getenv("GPT_LANG_HINT", "").strip()
lang_prefix = f"{lang_hint} " if lang_hint else ""

# Compose prompt
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": f"Explain the following {lang_prefix}code:\n\n{code}"}
]

# Call the chat completion API
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    max_tokens=500,
    temperature=0.3,
)

# Output the explanation
print("\n🧠 Code Explanation:\n")
print(response.choices[0].message.content.strip())
