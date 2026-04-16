# 🎬 Movie Recommender System

> *Find your next favorite film — by title, taste, or mood.*

A full-stack, content-based movie recommendation engine built with Python and Streamlit, containerized with Docker, and deployed on AWS EC2 via an automated CI/CD pipeline using GitHub Actions.

**Live Demo:** [[movierecommender-migo.app](http://13.61.26.140:8501)]

---

## 🚀 Deployment Architecture

```
Your Laptop 
        ↓  git push
GitHub Repository
        ↓
GitHub Actions (CI/CD Pipeline)
        ↓  SSH
AWS EC2 Server (Ubuntu)
        ↓
Docker Container
        ↓
Streamlit App (Port 8501)
        ↓
Browser → http://<(http://13.61.26.140:8501)>:8501
```

Every `git push` to `main` automatically:
1. SSHs into the EC2 server using a stored private key
2. Pulls the latest code
3. Stops and removes the old container
4. Rebuilds the Docker image
5. Runs the updated container — zero manual intervention

---

## ✨ Features

### 🏠 Home Page
Browse curated movie collections at a glance:
- **Most Voted** — movies with the highest number of audience votes
- **Most Rated** — top-rated films by score
- **Most Popular** — trending and widely watched titles

Each movie is displayed with its poster. Click any poster to open a detail panel showing:
`Genre · Rating · Runtime · Directed By · Cast · Overview`

---

### 🔍 Recommend Page
Search for any movie from the dataset using the dropdown search bar.
Hit **Recommend** and the system returns **5 similar movies with posters** — all computed using cosine similarity on TF-IDF movie tags.

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
TMDB 5000 Movie Dataset
        ↓
Feature Engineering → Tags (genres, cast, crew, keywords, overview)
        ↓
TF-IDF Vectorization (scikit-learn)
        ↓
Cosine Similarity Matrix → stored as similarity.pkl.gz
        ↓
User Query → Similarity Lookup → Top-N Recommendations
```

- **Recommend Page** — uses a precomputed cosine similarity matrix. Given a selected movie, fetches the top 5 closest movies by similarity score.
- **Mood Picker** — uses TF-IDF at query time. Mood keywords are vectorized and matched against all movie tags in real-time.

---

## 🗂️ Dataset

**TMDB 5000 Movie Dataset** — sourced from The Movie Database (TMDb) API via Kaggle.

Contains: movie titles, genres, cast, crew, keywords, overview, ratings, runtime, popularity, revenue, and more.

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3 |
| UI Framework | Streamlit |
| ML / NLP | scikit-learn (TF-IDF, Cosine Similarity) |
| Data | Pandas, Pickle, Gzip |
| Containerization | Docker |
| Cloud | AWS EC2 (Ubuntu) |
| CI/CD | GitHub Actions |
| Poster Storage | Pre-downloaded TMDB image URLs (`merged.json`) |

---

## 📦 Docker Setup

```dockerfile
FROM python:3.9
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run locally:
```bash
docker build -t movie-recommender .
docker run -p 8501:8501 movie-recommender
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

Located at `.github/workflows/deploy.yml`

On every push to `main`, the pipeline:
```bash
git pull
docker stop movie-recommender
docker rm movie-recommender
docker build -t movie-recommender .
docker run -d -p 8501:8501 --name movie-recommender movie-recommender
```

**Secrets required in GitHub:**
- `EC2_HOST` — public IP of your EC2 instance
- `EC2_USER` — typically `ubuntu`
- `EC2_SSH_KEY` — your private SSH key

---

## 🖥️ Local Setup

```bash
# Clone the repo
git clone https://github.com/119-sam/movierecommender-migo
cd movierecommender-migo

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Home.py
```

---

## 📁 Project Structure

```
├── Home.py                  # Main home page
├── pages/
│   ├── Recommend.py         # Content-based recommendation
│   └── MoodPicker.py        # Mood-based recommendation
├── similarity.pkl.gz        # Precomputed cosine similarity matrix
├── merged.json              # Movie metadata + poster URLs
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── deploy.yml       # CI/CD pipeline
```

---

## 🌐 Live on AWS

The app is hosted on an **AWS EC2 (Ubuntu)** instance with Docker.

Access it at:
```
http://<EC2-PUBLIC-IP>:8501
```

---

## 👩‍💻 Author

**Ansari Sumaiya**
[GitHub](https://github.com/119-sam) · [LinkedIn](https://linkedin.com/in/ansari-sumaiya-5b489432a)
