# Movie Recommendation System 🎬

A Content-Based Movie Recommendation System built using the TMDB 5000 dataset. Enter any movie and get personalized recommendations based on genres, cast, crew, keywords, and plot overview using cosine similarity.

## 🔍 Problem Statement
With thousands of movies available, users struggle to find movies similar to what they already like. This system solves that by recommending movies based on their content features.

## 🚀 What it does
- Takes a movie name as input
- Analyzes genres, cast, crew, keywords, and overview
- Recommends top similar movies using cosine similarity
- Interactive web interface for easy use

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing & cleaning |
| Scikit-learn | CountVectorizer + Cosine Similarity |
| NLTK | Text stemming & preprocessing |
| Streamlit | Interactive web app |
| Jupyter Notebook | EDA & model building |
| Pickle | Save trained model & data |

## 📁 Project Structure
```
├── notebook.ipynb              # EDA + feature engineering + model building
├── app.py                      # Streamlit web app
├── tmdb_5000_movies.csv        # Movies dataset
├── tmdb_5000_credits.csv       # Credits dataset
├── movies.pkl                  # Processed movies data
├── similarity.pkl              # Cosine similarity matrix
└── README.md                   # Project documentation
```

## ⚙️ How to Run

1. Clone the repo:
```bash
git clone https://github.com/ManishBairwa09/Movie-Recommendation-System.git
```

2. Install dependencies:
```bash
pip install pandas numpy scikit-learn nltk streamlit
```

3. Run the app:
```bash
streamlit run app.py
```

## 🔄 How it works

1. **Data Merging** — TMDB movies + credits datasets merged on title
2. **Feature Extraction** — genres, cast (top 3), director, keywords, overview extracted
3. **Tag Creation** — All features combined into a single "tags" column
4. **Text Preprocessing** — Stemming applied using NLTK Porter Stemmer
5. **Vectorization** — CountVectorizer converts tags into 5000-feature vectors
6. **Similarity Calculation** — Cosine similarity computed between all movie vectors
7. **Recommendation** — Top 5 most similar movies returned for any input movie

## 🎯 Key Features
- Content-based filtering using NLP techniques
- Feature engineering from cast, crew, genres, keywords & overview
- Text stemming for better similarity matching
- Cosine similarity for accurate recommendations
- Interactive Streamlit web interface

## 📊 Dataset
- **Source:** TMDB 5000 Movie Dataset (Kaggle)
- **Size:** 4809 movies after preprocessing
- **Features used:** title, genres, cast, crew, keywords, overview

## 🏷️ Tags
`content-based-filtering` `recommendation-system` `cosine-similarity` `nlp` `tmdb` `scikit-learn` `streamlit` `python` `machine-learning` `movie-recommendation`
