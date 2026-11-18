import streamlit as st
import joblib
import difflib
import scipy.sparse as sp
from sklearn.metrics.pairwise import linear_kernel

st.set_page_config(page_title="🎬 CineMatch", layout="wide")

IMG_URL = "https://image.tmdb.org/t/p/w500"

@st.cache_resource
def load_data():
    movies = joblib.load("movies.pkl")
    vector_tags = sp.load_npz("tfidf_matrix.npz")
    title_map = dict(zip(movies["title"].str.lower(), movies["title"]))
    return movies, vector_tags, title_map

movies, vector_tags, title_map = load_data()

def show_poster(path):
    if isinstance(path, str) and path.strip():
        st.image(IMG_URL + path, use_container_width=True)
    else:
        st.write("No poster")

def recommend(idx, n=10):
    scores = linear_kernel(vector_tags[idx], vector_tags).ravel()
    top = scores.argsort()[::-1][1:n+1]
    return movies.iloc[top]

st.title("🎬 CineMatch")
name = st.text_input("Type a movie name", placeholder="e.g. Inception")

if name:
    matches = movies[movies["title"].str.lower() == name.strip().lower()]

    if matches.empty:
        suggestions = difflib.get_close_matches(name.strip().lower(), list(title_map.keys()), n=5, cutoff=0.6)
        st.error("Movie not found.")
        if suggestions:
            st.write("Did you mean:", ", ".join(title_map[s] for s in suggestions))
    else:
        idx = matches["vote_count"].idxmax()
        chosen = movies.loc[idx]

        # Section 1: the movie the user typed
        left, right = st.columns([1, 4])
        with left:
            show_poster(chosen["poster_path"])
        with right:
            st.subheader(chosen["title"])
            st.write(f"Released: {str(chosen['release_date'])[:4]}")
            st.write(f"Rating: {chosen['vote_average']:.1f}")

        st.divider()
        st.subheader("You may also like")

        # Section 2: 10 recommendations, 2 rows x 5 columns
        results = recommend(idx, 10)
        for start in (0, 5):
            cols = st.columns(5)
            row_movies = results.iloc[start:start + 5]
            for col, (_, m) in zip(cols, row_movies.iterrows()):
                with col:
                    show_poster(m["poster_path"])
                    st.caption(f"**{m['title']}** ({str(m['release_date'])[:4]})  ⭐ {m['vote_average']:.1f}")