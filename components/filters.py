import streamlit as st


def get_filter_inputs():
    genre = st.selectbox("Genre", options=["Action", "Comedy", "Drama"], index=0)
    year = st.slider("Year", min_value=1950, max_value=2025, value=2025)
    language = st.selectbox("Language", options=["en", "es", "fr"], index=0)
    return genre, year, language
