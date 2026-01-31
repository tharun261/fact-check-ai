import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def ai_check(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return pred  # 0 = FAKE, 1 = REAL