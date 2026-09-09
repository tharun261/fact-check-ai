import os

model\_path = os.path.join(os.path.dirname(**file**), 'model.pkl')
model = pickle.load(open(model_path,'rb'))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def ai_check(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return pred  # 0 = FAKE, 1 = REAL
