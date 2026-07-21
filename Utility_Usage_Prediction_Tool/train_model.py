import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Load Dataset
df = pd.read_csv(
    "dataset/household_power_consumption.txt",
    sep=";",
    low_memory=False
)

print("Dataset Loaded Successfully!\n")
print(df.head())

print("\nDataset Shape:", df.shape)

# Replace ? with NaN
df.replace("?", pd.NA, inplace=True)

# Keep useful columns
df = df[[
    "Global_active_power",
    "Voltage",
    "Global_intensity"
]]

# Convert to numeric
df = df.apply(pd.to_numeric)

# Remove missing values
df.dropna(inplace=True)

print("\nCleaned Dataset Shape:", df.shape)

# Features and Target
X = df[["Voltage", "Global_intensity"]]
y = df["Global_active_power"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# Prediction
y_pred = model.predict(X_test)

print("\nR2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# Save Model
joblib.dump(model, "model/utility_model.pkl")

print("\nModel Saved Successfully!")