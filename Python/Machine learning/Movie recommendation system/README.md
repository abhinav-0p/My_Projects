# 🎬 CineMatch: Content-Based Movie Recommender

CineMatch recommends movies similar to one you type in. It compares movie descriptions, genres, keywords, cast and directors using **TF-IDF** and a **linear kernel** (dot product) similarity, and shows the results as a poster grid in a **Streamlit** web app.

🔗 **Live demo:** _add your Streamlit Cloud link here_

![CineMatch screenshot](screenshot.png)
_(add a screenshot of the app and save it as `screenshot.png`)_

---

## Features

- Type any movie name (case-insensitive) and get **10 similar movies**
- Shows the poster of the movie you searched, followed by the recommendations in a **5 × 2 poster grid**
- Displays release year and rating for every movie
- **"Did you mean...?" suggestions** when the title is misspelled
- Fast: the heavy processing is done once in the notebook, and the app only loads the saved results

---

## How it works

1. **Filter the data.** Keep only released, non-adult movies with at least 50 votes. This reduces the dataset from about 444k rows to about 27.8k movies, which removes obscure titles and keeps the similarity step fast.
2. **Build a text "tag" for each movie** by combining the overview, genres, keywords, cast and directors. Names are joined into single tokens (for example `Christopher Nolan` becomes `christophernolan`), so different people with the same first name don't match each other.
3. **Clean the text.** Convert to lowercase, expand contractions, remove punctuation, and remove stopwords.
4. **Convert text to numbers with TF-IDF.** Each movie becomes a vector. Words that are distinctive to a movie get a high weight, and very common words get a low one.
5. **Find similar movies.** For the chosen movie, `linear_kernel` computes its similarity score against every other movie (a dot product between TF-IDF vectors, which gives the same scores as cosine similarity because the vectors are already normalized). The 10 highest scores are the recommendations.
6. **Serve it with Streamlit.** The notebook saves the movie table and the TF-IDF matrix to files, and `app.py` loads them and shows the results.

```
Notebook (run once)                      app.py (runs on every search)
-------------------                      -----------------------------
load + filter + clean data               load movies.pkl and tfidf_matrix.npz
build tags, TF-IDF         --saves-->    user types a movie name
movies.pkl                               linear_kernel finds top 10 similar
tfidf_matrix.npz                         show posters in a 5 x 2 grid
```

---

## Tech stack

- **Python**
- **pandas**: data handling
- **NLTK**: stopwords
- **contractions**: expanding contractions
- **scikit-learn**: TF-IDF and similarity (`TfidfVectorizer`, `linear_kernel`)
- **SciPy / joblib**: saving the sparse matrix and the movie table
- **Streamlit**: web interface
- **difflib**: spelling suggestions

---

## Project structure

```
.
├── app.py                          # Streamlit app
├── movie_recommendation_main.ipynb # data cleaning, TF-IDF, saving the model files
├── movies.pkl                      # saved movie table (title, year, poster, rating, votes)
├── tfidf_matrix.npz                # saved TF-IDF matrix
├── requirements.txt
└── README.md
```

---

## Limitations

- **Content-based only.** It recommends by text similarity, not by what users actually watched or rated, so it can't learn personal taste.
- **Keyword matching, not meaning.** TF-IDF matches words, so it doesn't know that "spaceship" and "rocket" are related. Results can also include documentaries or short films that share a franchise's cast and keywords.
- **Popularity is not considered** when ranking, so a less popular movie with a very similar description can rank above a well-known one.
- **Exact title match.** If several movies share the same title, the one with the most votes is used.

## Future improvements

- Rank by a mix of similarity and popularity
- Use sentence embeddings (for example `sentence-transformers`) to capture meaning instead of just words
- Add filters for genre and release year
- Search by describing a plot instead of typing a title
- Add collaborative filtering with a ratings dataset

---

## Data and credits

- Dataset: [TMDB + IMDB Merged Movies Dataset](https://www.kaggle.com/datasets/ggtejas/tmdb-imdb-merged-movies-dataset) by ggtejas on Kaggle (license: CC BY-NC-SA 4.0)
- Poster images are loaded from the TMDB image server. This product uses TMDB data but is not endorsed or certified by TMDB.
