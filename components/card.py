import uuid
import streamlit as st


def show_movie_card(movie, on_add_to_watchlist=None, on_view_details=None):
    if not movie.get("poster_path"):
        return

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(f"https://image.tmdb.org/t/p/w200{movie['poster_path']}", width=100)
    with col2:
        st.write(f"**{movie['title']}**")
        if on_add_to_watchlist and st.button(
            "➕ Add to Watchlist", key=str(uuid.uuid4())
        ):
            on_add_to_watchlist(movie)
        if on_view_details and st.button("👁️ View Details", key=str(uuid.uuid4())):
            on_view_details(movie["id"])
