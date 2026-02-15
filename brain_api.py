import os
from groq import Groq

CATEGORIES = [
    "Housing & Rent", 
    "Utilities & Bills", 
    "Food & Dining", 
    "Transportation", 
    "Shopping", 
    "Entertainment", 
    "Credit Card Payment", 
    "Income & Refunds", 
    "Other"
]

def get_summary(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        f"You are VaultGuard, a friendly and supportive finance assistant. "
        f"Start with a warm greeting and a brief, encouraging overview of the user's month. "
        f"Use these categories: {', '.join(CATEGORIES)}. "
        f"Logic Rules: 'Mobile Payment' is a positive (+) Credit Card Payment. "
        f"'Hulu' and 'Disney' are Entertainment. 'Duke' is Utilities. "
        f"Show a clean Markdown table: Date | Description | Category | Amount."
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}]
    )
    return res.choices[0].message.content

def get_chart_data(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        f"Extract totals for: {', '.join(CATEGORIES)}. "
        f"Rules: 'Disney' and 'Hulu' are Entertainment. 'Duke' is Utilities. "
        f"Ignore 'Credit Card Payment' from pie chart totals. "
        f"The 'Disney $84' credit is actually a small recurring $5.38 or $7.00 amount; "
        f"only extract the actual numeric value found in the text. "
        f"Return ONLY JSON: {{'Category': Total}}."
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}],
        response_format={"type": "json_object"}
    )
    return res.choices[0].message.content