import streamlit as st
from services.watchlist import load_watchlist, toggle_watched, remove_movie


def show():
    st.title("✅ My Watchlist")

    watchlist = load_watchlist()

    if not watchlist:
        st.info("Your watchlist is empty.")
        return

    for item in watchlist:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.image(f"https://image.tmdb.org/t/p/w92{item['poster_path']}", width=50)
            st.write(f"**{item['title']}**")
        with col2:
            if st.button(
                "✅ Mark Watched" if not item["watched"] else "🔄 Unmark",
                key=f"toggle_{item['id']}",
            ):
                toggle_watched(item["id"])
                st.experimental_rerun()
        with col3:
            if st.button("🗑️ Remove", key=f"remove_{item['id']}"):
                remove_movie(item["id"])
                st.experimental_rerun()
