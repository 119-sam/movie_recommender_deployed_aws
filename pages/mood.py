import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import gzip 

# Set page config
st.set_page_config(page_title="Mood Recommender", layout="wide")


movie_posters = {
    13539: "https://image.tmdb.org/t/p/w500/shvubL3pIrCyEK22ZHrx00oNtCY.jpg",
    15544: "https://image.tmdb.org/t/p/w500/3N5XjwUITJo5MFhvWCJHVJt8pAg.jpg",
    13673: "https://image.tmdb.org/t/p/w500/q866vL3KhAjbkZH1enT7AoxmRHx.jpg",
    333348: "https://image.tmdb.org/t/p/w500/fPW1BHZhUEViOmDAHFfyLezoQdI.jpg",
    12281: "https://image.tmdb.org/t/p/w500/47icHsfwq7qpfPTuGwZxAtQ0olJ.jpg",
    9895: "https://image.tmdb.org/t/p/w500/s1etp9ZqcRqZVfonrdFJbQ6mgk9.jpg",
    10316: "https://image.tmdb.org/t/p/w500/w8t4UnJnC24S9ygoaFgmMzRbErd.jpg",
    355629: "https://image.tmdb.org/t/p/w500/sb7lZhOmQN5QrAVx4voyBDuPilM.jpg",
    10445: "https://image.tmdb.org/t/p/w500/5jTWY1M2O4Zhid4rLOpftzazRGn.jpg",
    10362: "https://image.tmdb.org/t/p/w500/skwYEUcxhUub9QCSwPDMvBySphS.jpg",
    76170: "https://image.tmdb.org/t/p/w500/8lzmovtARDXnE7kTDOum02i6fXv.jpg",
    77949: "https://image.tmdb.org/t/p/w500/9SJHeGRlpwkJknUMo7DPg7frrnH.jpg",
    25643: "https://image.tmdb.org/t/p/w500/ijRJlhAZ7QMkTIVAUkIY8stWfk1.jpg",
    16619: "https://image.tmdb.org/t/p/w500/tJVETEDAKgD3fEh88SHOvMvOQue.jpg",
    27585: "https://image.tmdb.org/t/p/w500/zTUQXwMn4ndt5AAcDvJCi14ZY2B.jpg",
    13072: "https://image.tmdb.org/t/p/w500/jTmCII6EnK1h0nLPusWvQnp9QTa.jpg",
    347764: "https://image.tmdb.org/t/p/w500/5zrBskQtkPzthObgssDuUTG7hcd.jpg",
    55831: "https://image.tmdb.org/t/p/w500/fUcoCzSGBTm2xHnGqH0D5kQV9lH.jpg",
    11661: "https://image.tmdb.org/t/p/w500/9Ka8lKCIiWjnZiMslPQeakS5UhW.jpg",
    9665: "https://image.tmdb.org/t/p/w500/pGDzBjZvzmSCIEduQBfESLMiwtp.jpg",
    300327: "https://image.tmdb.org/t/p/w500/aAfg4t3Aoz2KSfaN0q9vYqsYZBo.jpg",
    128: "https://image.tmdb.org/t/p/w500/cMYCDADoLKLbB83g4WnJegaZimC.jpg",
    45791: "https://image.tmdb.org/t/p/w500/fWzhqUMGva7sKENr4L6M1RC7BlA.jpg",
    80468: "https://image.tmdb.org/t/p/w500/3k8CeFdvTOiKaRCnXQ9I7WuazQi.jpg",
    186935: "https://image.tmdb.org/t/p/w500/cblCQ0h5oFYlufWoYeFJZAYm0bZ.jpg",
    34101: "https://image.tmdb.org/t/p/w500/xidkzvrJfBeZ6wVcVOxobZruiR7.jpg",
    14582: "https://image.tmdb.org/t/p/w500/2FMtSxzF2fR5dx5was9Kftjag0U.jpg",
    283686: "https://image.tmdb.org/t/p/w500/Lql2rnNRmKJrjq4FhEUh7IwkNd.jpg",
    1933: "https://image.tmdb.org/t/p/w500/p8g1vlTvpM6nr2hMMiZ1fUlKF0D.jpg",
    310933: "https://image.tmdb.org/t/p/w500/o8alLhpTJUKuFPEU7dECEUj1MNL.jpg",
    13937: "https://image.tmdb.org/t/p/w500/5vRn138vnZeUNFe32qTuPGKkVLR.jpg",
    54702: "https://image.tmdb.org/t/p/w500/l7JVY5uGMeOkEDNYIFLmZcEEQze.jpg",
    241257: "https://image.tmdb.org/t/p/w500/luHpMTmU1ygtEgdOTSSj0i9nd8E.jpg",
    15198: "https://image.tmdb.org/t/p/w500/bmg4sjOQswcrP5mPL9YzNom9cXx.jpg",
    11024: "https://image.tmdb.org/t/p/w500/5BrXCJrs22bR5KR6mLHluYo6y4m.jpg",
    63006: "https://image.tmdb.org/t/p/w500/uzqKhhSA6ypWwqsnZSwCs7C42sb.jpg",
    280092: "https://image.tmdb.org/t/p/w500/iDdGfdNvY1EX0uDdA4Ru77fwMfc.jpg",
    28260: "https://image.tmdb.org/t/p/w500/aXHsq5cSxdCySfTcuptN6HYWYHv.jpg",
    76726: "https://image.tmdb.org/t/p/w500/kdyrdFIt29FUmLIKvedAc2j4rpo.jpg",
    13827: "https://image.tmdb.org/t/p/w500/948AdP72iLQUjWvKp9r8981PT28.jpg",
    10153: "https://image.tmdb.org/t/p/w500/reR7C7EYe3DiHm5OYpA0ACUMDld.jpg",
    37206: "https://image.tmdb.org/t/p/w500/9FWxI20tzm9LuP3KT9cbmp5YN6Q.jpg",
    10285: "https://image.tmdb.org/t/p/w500/Aacq05foqiWdXqetFv02HBvMoJy.jpg",
    36047: "https://image.tmdb.org/t/p/w500/j77l405846qiLb8RGb1egu7ON3r.jpg",
    10383: "https://image.tmdb.org/t/p/w500/9DOq3KqGrNbqa3z5M8iDJ2wuaxJ.jpg"
}

# Mood definitions
mood_keywords = {
    "Happy 😊": "joy love friendship celebration victory",
    "Sad 😢": "loss heartbreak tragedy grief emotional",
    "Intense 🔥": "revenge anger war conflict fight",
    "Horror👻": "horror thriller suspense haunted mystery",
    "Thrilling 🎭": "twist unexpected discovery shocking reveal"
}


@st.cache_data
def load_data():
    try:
        
        movies = pickle.load(open('data/movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies)
        
        if 'tags' not in movies.columns:
            st.error("Error: 'tags' column not found")
            return None, None
            
        # Load compressed similarity matrix
        with gzip.open('similarity.pkl.gz', 'rb') as f:
            similarity = pickle.load(f)
            
        return movies, similarity
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

movies, similarity = load_data()  

if movies is None:
    st.stop()

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['tags'].astype(str))

def recommend_by_mood(mood):
    query = mood_keywords[mood]
    query_vec = tfidf.transform([query])
    similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    indices = similarity_scores.argsort()[-9:][::-1]  # Get top 9
    recommended = movies.iloc[indices]
    
    # Add poster URLs
    recommended['poster'] = recommended['movie_id'].map(movie_posters)
    return recommended[['title', 'movie_id', 'poster']]


st.title("🎭 Mood-Based Movie Recommender")

# Mood buttons
st.subheader("Select Your Mood:")
cols = st.columns(5)
moods = ["Happy 😊", "Sad 😢", "Intense 🔥", "Horror👻", "Thrilling 🎭"]
selected_mood = None

for i, mood in enumerate(moods):
    if cols[i].button(f"{mood}"):
        selected_mood = mood

# Display results in perfect 3x3 grid
if selected_mood:
    st.subheader(f"🍿 {selected_mood} Mood Movies")
    recommendations = recommend_by_mood(selected_mood)
    
    
    for row in range(0, 9, 3):
        cols = st.columns(3)
        for col in range(3):
            idx = row + col
            if idx < len(recommendations):
                movie = recommendations.iloc[idx]
                with cols[col]:
                    if pd.notna(movie['poster']):
                        st.image(
                            movie['poster'], 
                            width=200, 
                            caption=movie['title'],
                            use_container_width=True
                        )
                    else:
                        st.error(f"Poster missing for {movie['title']}")
                    st.caption(movie['title'])