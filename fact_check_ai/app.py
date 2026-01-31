from flask import Flask, render_template, request
from logic import final_decision

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",result=None)

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["news"]
    result = final_decision(text)
    return render_template("index.html", result=result, news=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)