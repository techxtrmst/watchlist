import streamlit as st
from services.tmdb import search_movies
from services.watchlist import add_movie
from components.card import show_movie_card
from components.filters import get_filter_inputs


def add(movie):
    if add_movie(movie):
        st.success(f"Added '{movie['title']}' to watchlist!")


def details(movie_id):
    st.session_state.selected_movie_id = movie_id
    st.rerun()


def show():
    st.title("🔍 All Shows")

    genre, year, language = get_filter_inputs()

    movies = search_movies(genre=genre, year=year, language=language)

    if not movies:
        st.info("No movies found with selected filters.")
        return

    # Grid: 4 columns per row
    for i in range(0, len(movies), 4):
        batch = movies[i : i + 4]
        cols = st.columns(4)
        for j, movie in enumerate(batch):
            with cols[j]:
                show_movie_card(
                    movie,
                    on_add_to_watchlist=add,
                    on_view_details=details,
                    key_suffix=f"_all_{i}_{j}",
                )
