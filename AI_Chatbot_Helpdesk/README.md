# 🤖 AI Chatbot for Internal Helpdesk

A Machine Learning and Flask-based chatbot that answers common employee queries using Natural Language Processing (NLP) and Machine Learning.

---

## 📌 Project Overview 

The **AI Chatbot for Internal Helpdesk** is designed to assist employees by providing instant answers to frequently asked questions (FAQs). The chatbot uses **TF-IDF Vectorization** and a **Logistic Regression** model to understand user queries and return the most relevant response.

This project demonstrates the complete workflow of building an NLP-based chatbot, from data preparation to deploying a web application using Flask.

---

## 🚀 Features

- 🤖 AI-powered FAQ Chatbot
- 💬 Instant response to employee queries
- 📝 FAQ Dataset
- 🔍 NLP Text Processing
- 📊 TF-IDF Vectorization
- 🧠 Logistic Regression Model
- 🌐 Flask Web Application
- 💾 Model Saving using Joblib
- ⚠️ Exception Handling

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Joblib
- HTML
- CSS

---

## 📂 Project Structure

```
AI_Chatbot_Helpdesk
│
├── dataset
│   └── faq_dataset.csv
│
├── model
│   ├── chatbot_model.pkl
│   └── vectorizer.pkl
│
├── templates
│   └── index.html
│
├── screenshots
│   ├── home_page.png
│   ├── password_reset_response.png
│   ├── office_timings_response.png
│   ├── leave_request_response.png
│   ├── project_structure.png
│   ├── training_model.png
│   └── flask_running_terminal.png
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 📊 Machine Learning Workflow

- Create FAQ Dataset
- Data Preprocessing
- TF-IDF Feature Extraction
- Train Logistic Regression Model
- Save Model using Joblib
- Load Model in Flask
- User Query Prediction
- Display Chatbot Response

---

## 🤖 Machine Learning Algorithm

- Logistic Regression

---

## ▶️ Installation

### Clone the repository

```bash
git clone https://github.com/aartiprajapati-ai/CODEVEDX.git
```

### Go to the project folder

```bash
cd AI_Chatbot_Helpdesk
```

### Install required libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train_model.py
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home_page.png)

---

### 🔐 Password Reset Response

![Password Reset](screenshots/password_reset_response.png)

---

### 🕒 Office Timings Response

![Office Timings](screenshots/office_timings_response.png)

---

### 📝 Leave Request Response

![Leave Request](screenshots/leave_request_response.png)

---

### 📂 Project Structure

![Project Structure](screenshots/project_structure.png)

---

### 🧠 Model Training

![Training Model](screenshots/training_model.png)

---

### 💻 Flask Running

![Flask Running](screenshots/flask_running_terminal.png)

---

## 📌 Future Improvements

- Voice-based Chatbot
- Database Integration
- User Authentication
- Admin Panel
- Multi-language Support
- AI-powered Intent Recognition

---

## 👩‍💻 Author

**Aarti Prajapati**

B.Tech CSE (Artificial Intelligence & Machine Learning)

IIMT University, Meerut

---

⭐ If you like this project, don't forget to give it a Star on GitHub!
