import streamlit as st
import pickle
import pandas as pd


# Load trained model
model = pickle.load(open("student_performance_model.pkl", "rb"))


st.title("Student Performance Prediction System")

st.write(
    "This application predicts student's final marks using Machine Learning."
)


study_hours = st.number_input(
    "Enter Study Hours",
    min_value=0,
    max_value=24
)

attendance = st.number_input(
    "Enter Attendance (%)",
    min_value=0,
    max_value=100
)

previous_marks = st.number_input(
    "Enter Previous Marks",
    min_value=0,
    max_value=100
)


if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks]
    })


    prediction = model.predict(input_data)

    st.success(
        f"Predicted Final Marks: {prediction[0]:.2f}"
    )