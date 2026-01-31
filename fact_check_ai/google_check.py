import requests

API_KEY = "c50b110f6cfc4e52b0dec290e02f07e5"  # Free: https://newsapi.org

def google_check(query):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "pageSize": 3,
        "apiKey": API_KEY
    }
    try:
        res = requests.get(url, params=params, timeout=5).json()
        if res.get("articles"):
            return True
    except:
        pass
    return False