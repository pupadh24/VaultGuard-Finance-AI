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

def get_summary(data, chart_json):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        f"You are VaultGuard, a friendly finance AI. "
        f"Here is the CORRECT spending data for this month: {chart_json}. "
        f"USE THESE NUMBERS ONLY. Do not invent new totals. "
        f"Give a warm greeting and summarize the spending based on these totals. "
        f"Include a Markdown table of the Top 3 spending categories."
    )
    
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}]
    )
    return res.choices[0].message.content

def get_chart_data(data):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = (
        f"Extract totals for these categories: {', '.join(CATEGORIES)}. "
        f"Rules: 'Disney' and 'Hulu' are Entertainment. 'Duke' is Utilities & Bills. "
        f"Ignore 'Credit Card Payment' from pie chart totals. "
        f"For Disney, use only the numeric value found ($5.38 or $7.00), ignore references to $84. "
        f"Return ONLY JSON: {{'Category': Total}}."
    )
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": data}],
        response_format={"type": "json_object"}
    )
    return res.choices[0].message.content