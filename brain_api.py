import os
from groq import Groq

def get_summary(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        "You are VaultGuard, a friendly finance AI "
        "Summarize the user's spending warmly and provide a Markdown table of the Top 3 transactions "
        "Rule: Positive numbers = Spending, Negative = Credits. Do not output JSON"
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}]
    )
    return res.choices[0].message.content

def get_chart_data(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        "You are a data extractor. Extract categories and totals from these transactions "
        "Return ONLY a JSON object. Example: {'Rent': 1200, 'Groceries': 150} "
        "Rule: Spent = Positive, Credits = Negative. Only use the final number per line"
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}],
        response_format={"type": "json_object"}
    )
    return res.choices[0].message.content