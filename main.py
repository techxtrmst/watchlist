import os
import sys
import streamlit as st

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

st.set_page_config(page_title="🎬 Watchlist App", layout="wide")

# Initialize session state for movie details
if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None

st.sidebar.title("Navigation")

# Handle movie details page
if st.session_state.selected_movie_id:
    if st.sidebar.button("← Back"):
        st.session_state.selected_movie_id = None
        st.rerun()

    from pages import show_details

    show_details.show()
else:
    page = st.sidebar.radio("Go to", ["🏠 Home", "🔍 All Shows", "✅ My Watchlist"])

    if page == "🏠 Home":
        from pages import home

        home.show()
    elif page == "🔍 All Shows":
        from pages import all_shows

        all_shows.show()
    elif page == "✅ My Watchlist":
        from pages import watchlist

        watchlist.show()
