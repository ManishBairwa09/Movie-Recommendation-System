import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

@st.cache_resource
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

try:
    movies, similarity = load_data()
except FileNotFoundError as e:
    st.error(f"Missing file: {e}")
    st.stop()

def fetch_poster(title):
    try:
        url = f"http://www.omdbapi.com/?t={requests.utils.quote(title)}&apikey=4335762"
        response = requests.get(url, timeout=5)
        data = response.json()
        poster = data.get('Poster')
        if poster and poster != 'N/A':
            return poster
    except Exception:
        pass
    return None

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    names = [movies.iloc[i[0]]['title'] for i in movie_list]
    return names

# ── UI ──────────────────────────────────────────────────────────────
st.title("🎬 Movie Recommender System")
st.markdown("Select a movie and click **Recommend**.")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    names = recommend(selected_movie)

    st.subheader("Movies you might like:")
    cols = st.columns(5)

    for col, name in zip(cols, names):
        with col:
            poster_url = fetch_poster(name)
            if poster_url:
                st.image(poster_url, width=150)
            else:
                st.markdown(
                    '<div style="background:#1e1e2e;border-radius:12px;padding:40px 10px;'
                    'text-align:center;color:#fff;border:1px solid #444;">🎬</div>',
                    unsafe_allow_html=True
                )
            st.caption(name)