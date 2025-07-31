import streamlit as st
from services.watchlist import load_watchlist, toggle_watched, remove_movie


def show_watchlist_card(item):
    with st.container():
        st.image(
            f"https://image.tmdb.org/t/p/w200{item['poster_path']}",
            use_container_width=True,
        )
        st.markdown(f"**{item['title']}**")
        
        # Show watched status
        status = "✅ Watched" if item["watched"] else "⏳ Not Watched"
        st.caption(status)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(
                "✅ Mark Watched" if not item["watched"] else "🔄 Unmark",
                key=f"toggle_{item['id']}",
                use_container_width=True,
            ):
                toggle_watched(item["id"])
                st.rerun()
        with col2:
            if st.button(
                "🗑️ Remove", 
                key=f"remove_{item['id']}",
                use_container_width=True,
            ):
                remove_movie(item["id"])
                st.rerun()


def show():
    st.title("✅ My Watchlist")

    watchlist = load_watchlist()

    if not watchlist:
        st.info("Your watchlist is empty.")
        return

    # Grid: 4 columns per row (same as home page)
    for i in range(0, len(watchlist), 4):
        batch = watchlist[i : i + 4]
        cols = st.columns(4)
        for j, item in enumerate(batch):
            with cols[j]:
                show_watchlist_card(item)
