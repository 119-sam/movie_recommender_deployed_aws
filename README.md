# 🎬 Movie Recommender System

A content-based movie recommendation web app built with Python and Streamlit, powered by TF-IDF vectorization and cosine similarity on the TMDB 5000 dataset.

🚀 **Live Demo → [movierecommender-migo.streamlit.app](https://movierecommender-migo.streamlit.app/)**

---

## ✨ Features

### 🏠 Home Page
Browse curated movie collections at a glance:
- **Most Voted** — movies with the highest number of audience votes
- **Most Rated** — top-rated films by score
- **Most Popular** — trending and widely watched titles

Each movie is displayed with its poster. Click any poster to open a detail panel showing:
> Genre · Rating · Runtime · Directed By · Cast · Overview

---

### 🔍 Recommend Page
Search for any movie from the dataset using the dropdown search bar.

Hit **Recommend** and the system returns **5 similar movies** with posters — all computed using cosine similarity on TF-IDF movie tags.

---

### 🎭 Mood Picker Page
Not sure what to watch? Pick a mood and let the app decide.

| Mood | Vibe |
|------|------|
| Happy 😊 | Joy, love, friendship, celebration |
| Sad 😢 | Loss, heartbreak, grief, tragedy |
| Intense 🔥 | Revenge, war, conflict, anger |
| Horror 👻 | Suspense, haunted, mystery, thriller |
| Thrilling 🎭 | Twists, shocking reveals, unexpected turns |

Returns a **3×3 grid of 9 movies** matching your selected mood.

---

## 🧠 How It Works

```
Movie Dataset (TMDB 5000)
        ↓
Feature Engineering → Tags (genres, cast, crew, keywords, overview)
        ↓
TF-IDF Vectorization (sklearn)
        ↓
Cosine Similarity Matrix → stored as similarity.pkl.gz
        ↓
User Query → Similarity Lookup → Top-N Recommendations
```

- **Recommend Page**: uses a precomputed cosine similarity matrix. Given a selected movie, it fetches the top 5 closest movies by similarity score.
- **Mood Picker**: uses TF-IDF at query time — mood keywords are vectorized and matched against all movie tags in real-time.

---

## 🗂️ Dataset

**[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** — sourced from The Movie Database (TMDb) API via Kaggle.

Contains: movie titles, genres, cast, crew, keywords, overview, ratings, runtime, popularity, revenue, and more.

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3 |
| UI Framework | Streamlit |
| ML / NLP | scikit-learn (TF-IDF, Cosine Similarity) |
| Data | Pandas, Pickle, Gzip |
| Poster Storage | Pre-downloaded TMDB image URLs stored in `merged.json` |
| Deployment | Streamlit Community Cloud |

---

## 📁 Project Structure

```
movie-recommender/
│
├── data/
│   ├── movie_dict.pkl        # Processed movie dataframe (pickled)
│   └── movie_list.pkl        # Movie titles list (pickled)
│
├── similarity.pkl.gz         # Compressed cosine similarity matrix
├── merged.json               # movie_id → poster URL mapping
│
├── Home.py                   # Home page (curated collections)
├── pages/
│   ├── Recommend.py          # Cosine similarity recommender
│   └── MoodPicker.py         # Mood-based recommender
│
└── requirements.txt
```

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run Home.py
```

> **Note:** The `similarity.pkl.gz` file and `data/` folder must be present locally for the app to work.

---

## 📦 Requirements

```
streamlit
pandas
scikit-learn
```

---

## 🙏 Acknowledgements

- Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) via Kaggle
- Poster images sourced from [The Movie Database (TMDb)](https://www.themoviedb.org/) API
- Built as a personal project to explore content-based filtering and NLP-based recommendation systems
