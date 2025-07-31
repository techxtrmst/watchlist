import os
import sys
import streamlit as st


project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

st.set_page_config(page_title="🎬 Watchlist App", layout="wide")
st.sidebar.title("Navigation")
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
