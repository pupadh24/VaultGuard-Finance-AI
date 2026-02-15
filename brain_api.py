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
        f"You are VaultGuard Finance AI. Summarize the spending. "
        f"Classify transactions into these categories: {', '.join(CATEGORIES)}. "
        f"Note: 'Mobile Payment' is a Credit Card Payment. 'Duke' is Utilities. "
        f"Show a Markdown table of all transactions with Date, Description, Category, and Amount."
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}]
    )
    return res.choices[0].message.content

def get_chart_data(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        f"Act as a data processor. Group all transactions into these categories: {', '.join(CATEGORIES)}. "
        f"Return ONLY a JSON object where keys are category names and values are totals. "
        f"Exclude 'Credit Card Payment' from the totals. "
        f"Ensure all values are positive numbers."
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}],
        response_format={"type": "json_object"}
    )
    return res.choices[0].message.content