# 🎬 Smart Movie Recommendation System

## Project Overview

This project is an AI-based Movie Recommendation System that recommends similar movies based on the selected movie.

## Features

- Movie Recommendation
- Content-Based Filtering
- Streamlit Web App
- TMDB Dataset
- Fast Recommendations

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle

## Project Structure

```
Smart_Recommendation_System/
│
├── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│   └── movies.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

## Generate Model Files

The `similarity.pkl` file is not included because it exceeds GitHub's file size limit.

To generate it, run:

```bash
python train_model.py
```

This will generate:

- movies.pkl
- similarity.pkl

## Run the Application

```bash
streamlit run app.py
```