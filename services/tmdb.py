import os
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def _get(endpoint: str, params: dict = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/{endpoint}"
    params = params or {}
    params["api_key"] = TMDB_API_KEY
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_trending_movies() -> List[Dict[str, Any]]:
    return _get("trending/movie/week").get("results", [])[:10]


def get_popular_movies() -> List[Dict[str, Any]]:
    return _get("movie/popular").get("results", [])[:10]


def get_upcoming_movies() -> List[Dict[str, Any]]:
    return _get("movie/upcoming").get("results", [])[:10]


def search_movies(
    query: str = None, genre: str = None, year: int = None, language: str = "en"
) -> List[Dict[str, Any]]:
    if query:
        params = {"query": query, "language": language}
        if year:
            params["year"] = year
        data = _get("search/movie", params)
    else:
        params = {"language": language}
        if year:
            params["year"] = year
        data = _get("discover/movie", params)
    return data.get("results", [])


def get_movie_details(movie_id: int) -> Dict[str, Any]:
    return _get(f"movie/{movie_id}")


def get_movie_cast(movie_id: int) -> List[Dict[str, Any]]:
    data = _get(f"movie/{movie_id}/credits")
    return data.get("cast", [])[:10]
