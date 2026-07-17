import streamlit as st
import pickle

# Load Data
movies = pickle.load(open('model/movies.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Streamlit UI
st.set_page_config(page_title="Smart Movie Recommendation System")

st.set_page_config(
    page_title="Smart Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Smart Movie Recommendation System")
st.markdown("### Get movie recommendations based on your favorite movie")

st.sidebar.title("About")
st.sidebar.info(
    """
    AI/ML Internship Project
    
    • Content-Based Recommendation System
    • Machine Learning
    • Cosine Similarity
    • CountVectorizer
    """
)

selected_movie = st.selectbox(
    "Choose a Movie",
    movies['title'].values
)

if st.button("🎯 Recommend Movies"):
    recommendations = recommend(selected_movie)

    st.success("Top 5 Recommended Movies")

    for movie in recommendations:
        st.write("✅", movie)

st.markdown("---")
st.caption("Developed by Aarti Prajapati | CodeVedX AI/ML Internship")