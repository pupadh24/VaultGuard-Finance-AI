import os

def chat(data):
    if os.environ.get("STREAMLIT_CLOUD"):
        import brain_api
        return brain_api.chat(data)
    else:
        try:
            import brain_local
            return brain_local.chat(data)
        except ImportError:
            import brain_api
            return brain_api.chat(data)