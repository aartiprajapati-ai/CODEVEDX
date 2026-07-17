from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

import pandas as pd

# Load datasets
fake = pd.read_csv("dataset/Fake.csv")
true = pd.read_csv("dataset/True.csv")

# Display first 5 rows
print("Fake News Dataset:")
print(fake.head())

print("\nTrue News Dataset:")
print(true.head())

# Display dataset shapes
print("\nFake Dataset Shape:", fake.shape)
print("True Dataset Shape:", true.shape)
# Add labels
fake["label"] = 0
true["label"] = 1

# Merge datasets
data = pd.concat([fake, true], axis=0)

# Shuffle dataset
data = data.sample(frac=1, random_state=42)

# Reset index
data.reset_index(drop=True, inplace=True)

print("\nMerged Dataset Shape:", data.shape)
print(data.head())
# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())
# Keep only required columns
data["content"] = data["title"] + " " + data["text"]

data = data[["content", "label"]]

print("\nSelected Columns:")
print(data.head())
# Split features and labels
X = data["content"]
y = data["label"]

print("\nNumber of News Articles:", len(X))
import re

# Text Cleaning Function
def clean_text(text):
    text = text.lower()                     # Lowercase
    text = re.sub(r'http\S+', '', text)     # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text) # Remove special characters
    text = re.sub(r'\s+', ' ', text)        # Remove extra spaces
    return text
# Apply text cleaning
X = X.apply(clean_text)

print("\nCleaned Text:")
print(X.head())
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))
# Convert text into numbers
vectorizer = TfidfVectorizer(stop_words='english')

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("\nTF-IDF Completed")
print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)
# Train Machine Learning Model
model = LogisticRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")
# Prediction
y_pred = model.predict(X_test)
# Model Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
# Save ML Model
joblib.dump(model, "model/model.pkl")

# Save TF-IDF Vectorizer
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\nModel Saved Successfully!")