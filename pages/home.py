import streamlit as st
from services.watchlist import add_movie
from components.card import show_movie_card
from services.tmdb import (
    get_trending_movies,
    get_popular_movies,
    get_upcoming_movies,
)


def add(movie):
    if add_movie(movie):
        st.success(f"Added '{movie['title']}' to watchlist!")


def details(movie_id):
    st.session_state.selected_movie_id = movie_id
    st.rerun()


def show_section(title, movies, section_key):
    st.subheader(title)
    if not movies:
        st.info("No movies found.")
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
                    key_suffix=f"_{section_key}_{i}_{j}",
                )


def show():
    st.title("🏠 Home")

    show_section("🔥 Trending", get_trending_movies(), "trend")
    show_section("🌟 Popular", get_popular_movies(), "pop")
    show_section("📅 Upcoming", get_upcoming_movies(), "upcoming")
