import os
from groq import Groq
import re

def chat(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = (
        "You are VaultGuard. 1. Summarize the spending warmly. "
        "2. List top transactions in a table. "
        "3. Math Rule: Positive = Spent, Negative = Credit. "
        "4. End with: CHART_DATA: {'Category': Amount}"
    )

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": data}
        ]
    )
    return response.choices[0].message.content