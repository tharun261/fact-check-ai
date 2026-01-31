import wikipediaapi

# Specify user_agent to avoid Wikipedia error
wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="FactCheckAI/1.0 (https://yourwebsite.com)"
)

def wiki_check(query):
    page = wiki.page(query)
    if page.exists():
        return True
    return False