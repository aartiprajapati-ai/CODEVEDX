import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load Dataset
df = pd.read_csv("dataset/faq_dataset.csv")

# Features and Labels
X = df["Question"]
y = df["Answer"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train Model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save Model
joblib.dump(model, "model/chatbot_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model trained and saved successfully!")