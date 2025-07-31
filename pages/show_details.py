import streamlit as st
from services.tmdb import get_movie_details


def show():
    query_params = st.experimental_get_query_params()
    movie_id = query_params.get("id", [None])[0]

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
        use_column_width=True,
    )
    st.title(movie["title"])
    st.write(movie["overview"])
    st.write(f"⭐ {movie['vote_average']} / 10")
    st.write(f"📅 Release Date: {movie['release_date']}")
    st.write(f"🎭 Genres: {', '.join(g['name'] for g in movie['genres'])}")
