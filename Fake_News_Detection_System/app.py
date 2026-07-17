import streamlit as st
import joblib
import re

# Load trained model and vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Text Cleaning Function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Page Title
st.set_page_config(page_title="Fake News Detection", page_icon="📰")

st.title("📰 AI Based Fake News Detection Tool")
st.write("Enter a news article below to check whether it is **Fake** or **Real**.")

# User Input
news = st.text_area("Enter News Text", height=200)

if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:

        # Clean text
        cleaned_news = clean_text(news)

        # Convert to TF-IDF
        vector = vectorizer.transform([cleaned_news])

        # Prediction
        prediction = model.predict(vector)[0]

        # Confidence Score
        probability = model.predict_proba(vector)[0]
        confidence = max(probability) * 100

        # Debug Value
        st.write("Prediction Value:", prediction)

        # Display Result
        if prediction == 0:
            st.error("🚨 Fake News")
        else:
            st.success("✅ Real News")

        st.write(f"**Confidence Score:** {confidence:.2f}%")