import os

def chat(data):
    if os.environ.get("STREAMLIT_CLOUD"):
        import brain_api
        summary = brain_api.get_summary(data)
        chart_json = brain_api.get_chart_data(data)
        return f"{summary} ||| {chart_json}"
    else:
        import brain_local
        return brain_local.chat(data)