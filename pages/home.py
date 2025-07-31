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
    st.experimental_set_query_params(page="show_details", id=movie_id)


def show():
    st.title("🏠 Home")

    st.subheader("🔥 Trending")
    for movie in get_trending_movies():
        show_movie_card(movie, on_add_to_watchlist=add, on_view_details=details)

    st.subheader("🌟 Popular")
    for movie in get_popular_movies():
        show_movie_card(movie, on_add_to_watchlist=add, on_view_details=details)

    st.subheader("📅 Upcoming")
    for movie in get_upcoming_movies():
        show_movie_card(movie, on_add_to_watchlist=add, on_view_details=details)
