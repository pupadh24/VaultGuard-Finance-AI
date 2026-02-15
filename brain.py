import os

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

def chat(data):
    if os.environ.get("STREAMLIT_CLOUD"):
        import brain_api
        summary = brain_api.get_summary(data)
        chart_json = brain_api.get_chart_data(data)
        return f"{summary} ||| {chart_json}"
    else:
        try:
            import brain_local
            return brain_local.chat(data)
        except ModuleNotFoundError:
            import brain_api
            summary = brain_api.get_summary(data)
            chart_json = brain_api.get_chart_data(data)
            return f"{summary} ||| {chart_json}"