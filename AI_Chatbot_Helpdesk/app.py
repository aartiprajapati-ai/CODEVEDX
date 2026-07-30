from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load Model
model = joblib.load("model/chatbot_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    user_input = request.form["message"]

    vector = vectorizer.transform([user_input])

    prediction = model.predict(vector)

    return render_template(
        "index.html",
        user_input=user_input,
        bot_reply=prediction[0]
    )


if __name__ == "__main__":
    app.run(debug=True)