import streamlit as st
from services.tmdb import get_movie_details


def show():
    movie_id = st.session_state.get("selected_movie_id")

    if not movie_id:
        st.error("No movie selected.")
        return

    try:
        movie = get_movie_details(movie_id)
    except Exception:
        st.error("Failed to load movie details.")
        return

    st.image(
        f"https://image.tmdb.org/t/p/w500{movie['backdrop_path']}",
        use_container_width=True,
    )
    st.title(movie["title"])
    st.write(movie["overview"])
    st.write(f"⭐ {movie['vote_average']} / 10")
    st.write(f"📅 Release Date: {movie['release_date']}")
    st.write(f"🎭 Genres: {', '.join(g['name'] for g in movie['genres'])}")
