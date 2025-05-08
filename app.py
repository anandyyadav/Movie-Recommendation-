import streamlit as st
import pickle
import pandas as pd
import requests
from requests.exceptions import RequestException

# --- Configuration ---
PAGE_TITLE = "  Movie Recommendation System"
HEADER_TITLE = "<h1 style='text-align: center; color: #FF4B4B;'>🎬 Movie Recommendation System </h1>"
RECOMMEND_BUTTON_TEXT = "✨ Find Recommendations"
NO_POSTER_URL = "https://via.placeholder.com/500x750?text=No+Poster+Available"
TMDB_API_KEY = "a87776cc525d33e078e1075fb3905d9a"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500/"
NUM_RECOMMENDATIONS = 5


# --- Functions ---
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        poster_path = data.get('poster_path')
        return f"{POSTER_BASE_URL}{poster_path}" if poster_path else NO_POSTER_URL
    except RequestException as e:
        st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
        return NO_POSTER_URL
    except KeyError:
        st.warning("No poster found for this movie.")
        return NO_POSTER_URL


def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Get rating and genres from the movie data
        rating = data.get('vote_average', 'N/A')
        genres = ', '.join([genre['name'] for genre in data.get('genres', [])])

        return rating, genres
    except RequestException as e:
        st.error(f"Error fetching details for movie ID {movie_id}: {e}")
        return 'N/A', 'N/A'
    except KeyError:
        st.warning("Missing details for this movie.")
        return 'N/A', 'N/A'


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        similarity_scores = sorted(
            list(enumerate(similarity[movie_index])),
            reverse=True,
            key=lambda x: x[1]
        )[1:NUM_RECOMMENDATIONS + 1]

        recommended_movies = []
        recommended_posters = []
        recommended_ratings = []
        recommended_genres = []

        for i in similarity_scores:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_posters.append(fetch_poster(movie_id))

            # Fetch movie details like rating and genres
            rating, genres = fetch_movie_details(movie_id)
            recommended_ratings.append(rating)
            recommended_genres.append(genres)

        return recommended_movies, recommended_posters, recommended_ratings, recommended_genres
    except IndexError:
        st.error(f"Oops! '{movie}' doesn't seem to be in our movie list. Please try another title.")
        return [], [], [], []
    except Exception as e:
        st.error(f"An unexpected error occurred while generating recommendations: {e}")
        return [], [], [], []


# --- Load Data ---
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error(
        "Error: One or more data files (movie_dict.pkl, similarity.pkl) not found. Please ensure they are in the same directory as the script.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while loading data: {e}")
    st.stop()

# --- Streamlit UI ---
st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.markdown(HEADER_TITLE, unsafe_allow_html=True)

# Movie selection with improved styling
st.markdown("<h3 style='color: #FFD700;'>✨ Let's Find Your Next Movie! </h3>", unsafe_allow_html=True)
selected_movie_name = st.selectbox(
    "",
    movies['title'].values,
    format_func=lambda title: title.title()  # Display movie titles in Title Case
)

# Recommendation button with styling
if st.button(RECOMMEND_BUTTON_TEXT):
    recommended_movies, recommended_posters, recommended_ratings, recommended_genres = recommend(selected_movie_name)

    if recommended_movies:
        st.markdown("<h2 style='color: #333;'>🍿 You might also like:</h2>", unsafe_allow_html=True)
        cols = st.columns(NUM_RECOMMENDATIONS)
        for i in range(NUM_RECOMMENDATIONS):
            with cols[i]:
                st.image(recommended_posters[i], use_container_width=True)
                st.markdown(f"<p style='text-align: center; font-weight: bold;'>{recommended_movies[i].title()}</p>",
                            unsafe_allow_html=True)
                st.markdown(f"**Rating**: {recommended_ratings[i]}/10")
                st.markdown(f"**Genres**: {recommended_genres[i]}")
    else:
        st.info("No recommendations found for the selected movie.")

# --- Footer ---
st.markdown("<hr style='border-top: 2px solid #ccc;'>", unsafe_allow_html=True)
