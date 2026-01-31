from google_check import google_check
from wiki_check import wiki_check
from ai_check import ai_check

def final_decision(text):
    if google_check(text) or wiki_check(text):
        return "✅ TRUE – Verified from trusted sources"
    if ai_check(text) == 0:
        return "❌ FALSE – AI detected fake pattern"
    return "⚠️ CAN'T IDENTIFY – No sufficient evidence found"