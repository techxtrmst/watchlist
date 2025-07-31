import streamlit as st
from services.tmdb import get_movie_details, get_movie_cast


def show():
    movie_id = st.session_state.get("selected_movie_id")

    if not movie_id:
        st.error("No movie selected.")
        return

    try:
        movie = get_movie_details(movie_id)
        cast = get_movie_cast(movie_id)
    except Exception:
        st.error("Failed to load movie details.")
        return

    # Movie backdrop
    if movie.get("backdrop_path"):
        st.image(
            f"https://image.tmdb.org/t/p/w500{movie['backdrop_path']}",
            use_container_width=True,
        )

    # Movie details
    st.title(movie["title"])
    st.write(movie["overview"])

    # Movie info in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"⭐ {movie['vote_average']:.1f} / 10")
    with col2:
        st.write(f"📅 {movie['release_date']}")
    with col3:
        st.write(f"⏱️ {movie.get('runtime', 'N/A')} min")

    # Genres
    if movie.get("genres"):
        st.write(f"🎭 **Genres:** {', '.join(g['name'] for g in movie['genres'])}")

    # Cast section
    if cast:
        st.subheader("🎬 Cast")
        cast_cols = st.columns(5)  # Show 5 cast members per row
        for i, actor in enumerate(cast):
            with cast_cols[i % 5]:
                if actor.get("profile_path"):
                    st.image(
                        f"https://image.tmdb.org/t/p/w185{actor['profile_path']}",
                        use_container_width=True,
                    )
                else:
                    st.write("🎭")  # Placeholder for missing photo
                st.write(f"**{actor['name']}**")
                st.caption(actor["character"])
