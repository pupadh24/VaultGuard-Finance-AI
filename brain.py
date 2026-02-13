import ollama

def chat(data):
    try:
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': 'You are VaultGuard Finance AI. Your goal is to answer their questions without judging them. Be nice and warm.'},
            {'role': 'user', 'content': data},
        ])
        return response['message']['content']
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(chat("Test transaction"))