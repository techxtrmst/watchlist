import streamlit as st


def show_movie_card(
    movie, on_add_to_watchlist=None, on_view_details=None, key_suffix=""
):
    if not movie.get("poster_path"):
        return

    with st.container():
        st.image(
            f"https://image.tmdb.org/t/p/w200{movie['poster_path']}",
            use_container_width=True,
        )
        st.markdown(f"**{movie['title']}**")

        col1, col2 = st.columns(2)
        with col1:
            if on_add_to_watchlist and st.button(
                "➕ Watchlist",
                key=f"watchlist_{movie['id']}{key_suffix}",
                use_container_width=True,
            ):
                on_add_to_watchlist(movie)
        with col2:
            if on_view_details and st.button(
                "👁️ Details",
                key=f"details_{movie['id']}{key_suffix}",
                use_container_width=True,
            ):
                on_view_details(movie["id"])
