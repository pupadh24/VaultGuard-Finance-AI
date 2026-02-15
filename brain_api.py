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
        "You are VaulGuard, a Precision Financial Parser. Extract totals for these categories: "
        "Housing, Utilities, Food, Entertainment, Shopping. "
        "CRITICAL RULES: "
        "1. 'MOBILE PAYMENT' = Credit Card Bill Pay. EXCLUDE from spending totals. "
        "2. 'DUKE ENERGY' = Utilities. This is a PAYMENT (+), not a credit (-). "
        "3. 'Hulu' or 'Disney' = Entertainment. "
        "4. IGNORE the $84.00 Disney amount. Only extract the literal dollar value next to it in the text ($5.38 or $7.00). "
        "5. Return ONLY raw JSON: {'Category': Amount}."
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