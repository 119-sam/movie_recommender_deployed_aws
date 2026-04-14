import streamlit as st
import pickle
import streamlit.components.v1 as components

# Load the movie details dictionary
try:
    movie_details = pickle.load(open("data/movie_details.pkl", "rb"))
except Exception as e:
    st.error(f"Failed to load movie data: {e}")
    st.stop()


clicked_id = st.query_params.get("id", None)
clicked_id = int(clicked_id) if clicked_id and clicked_id.isdigit() else None


manual_posters = {
    94: "https://image.tmdb.org/t/p/w500//r7vmZjiyZw9rpJMQJdXpjgiCOk9.jpg",
    95: "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    788: "https://image.tmdb.org/t/p/w500/fSRb7vyIP8rQpL0I47P3qUsEKX3.jpg",
    96: "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
    65: "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    0:  "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
    1883: "https://image.tmdb.org/t/p/w500/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
    2973: "https://image.tmdb.org/t/p/w500/lxvY6as28ykgbPEuvZ5T29am99L.jpg",
    127: "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"
}


if clicked_id and clicked_id in movie_details:
    movie = movie_details[clicked_id]
    
    
    movie['poster'] = manual_posters.get(clicked_id, "default_poster_url.jpg")
    
    st.set_page_config(page_title=movie['title'], layout="centered")
    
    
    poster_col, details_col = st.columns([1, 3])
    
    with poster_col:
        
        st.markdown(
            f"""
            <div style='box-shadow: 0 4px 8px rgba(0,0,0,0.2); border-radius: 8px;'>
                <img src="{movie['poster']}" style="width: 100%; border-radius: 8px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with details_col:
        
        st.markdown(
            f"""
            <h1 style='background: linear-gradient(45deg, #ff4b4b, #ff7b4b);
                      -webkit-background-clip: text;
                      -webkit-text-fill-color: transparent;
                      margin-bottom: 20px;'>
                {movie['title']}
            </h1>
            """,
            unsafe_allow_html=True
        )
        
        
        st.markdown(f"📅 **Release Date:** {movie['release_date']}")
        st.markdown(f"🎭 **Genre:** {movie['genres']}")
        st.markdown(f"⭐ **Rating:** {movie['vote_average']}/10")
        st.markdown(f"⏱️ **Runtime:** {movie['runtime']} min")
        
       
        if 'crew' in movie:
          st.markdown(
            f"""
            <div style='background-color: #2b2b2b; 
                      padding: 10px; 
                      border-radius: 8px;
                      margin: 10px 0;'>
                🎬 <span style='font-weight: bold; color: #ff4b4b;'>Directed by:</span> 
                <span style='color: white;'>{movie['crew']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if 'cast' in movie:
           st.markdown(
            f"""
            <div style='background-color: #2b2b2b; 
                      padding: 10px; 
                      border-radius: 8px;
                      margin: 10px 0;'>
                👥 <span style='font-weight: bold; color: #ff4b4b;'>Cast:</span> 
                <span style='color: white;'>{movie['cast']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        
        
        st.markdown(
            f"""
            <div style='border-left: 4px solid #ff4b4b;
                      padding-left: 15px;
                      margin: 20px 0;'>
                <h3 style='color: #ff4b4b;'>📖 Overview</h3>
                <p style='font-style: italic; line-height: 1.6;'>
                    {movie['overview']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Back button 
    st.markdown(
        """
        <style>
            .back-button:hover {
                background-color: #ff4b4b !important;
                color: white !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.button("🔙 Back to Home", 
             on_click=lambda: st.query_params.clear(),
             key="back_button",
             help="Return to the main page")

# Show Homepage with Top Movies 
else:
    st.set_page_config(page_title="MovieMate 🎬", layout="centered")
    st.title("🎬 Welcome to MovieMate")
    st.markdown("## 🌟 Handpicked Top Movies Just For You")

    
    sections = {
        "🔥 Most Popular Movies": [
            {"id": 94, "title": "Guardians of the Galaxy"},
            {"id": 95, "title": "Interstellar"},
            {"id": 788, "title": "Deadpool"},
        ],
        "🗳️ Most Voted Movies": [
            {"id": 96, "title": "Inception"},
            {"id": 65, "title": "The Dark Knight"},
            {"id": 0, "title": "Avatar"},
        ],
        "🏆 Top Rated Movies": [
            {"id": 1883, "title": "The Shawshank Redemption"},
            {"id": 2973, "title": "There Goes My Baby"},
            {"id": 127, "title": "Mad Max: Fury Road"},
        ],
    }

    
    # Display posters 
    for section_title, movies in sections.items():
        st.markdown(f"### {section_title}")
        cols = st.columns(3)
        
        for idx, movie in enumerate(movies):
            with cols[idx % 3]:
                poster_url = manual_posters.get(movie['id'], "")
                st.markdown(
                    f"""
                    <div style='text-align: center; margin-bottom: 20px;'>
                        <a href="/?id={movie['id']}" target="_self">
                            <img src="{poster_url}" 
                                 style="width: 100%; 
                                        border-radius: 10px; 
                                        height: 300px; 
                                        object-fit: cover;
                                        transition: transform 0.3s;"
                                 onmouseover="this.style.transform='scale(1.03)'"
                                 onmouseout="this.style.transform='scale(1)'">
                        </a>
                        <p style='font-weight: bold; 
                                 margin-top: 8px;
                                 font-size: 16px;'>
                            {movie['title']}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )