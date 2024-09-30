import requests

def ask_ai(question):
    try:
        # Replace 'YOUR_API_KEY' and 'API_ENDPOINT' with your actual API key and endpoint
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer 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"},
            json={"prompt": question, "max_tokens": 100}
        )
        ai_response = response.json().get('choices')[0].get('text')
        return ai_response
    except requests.exceptions.RequestException:
        return "No internet connection."
