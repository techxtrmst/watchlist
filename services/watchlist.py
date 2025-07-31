import os
import json
from datetime import date
from typing import List, Dict, Any


WATCHLIST_FILE = "data/watchlist.json"


def _ensure_watchlist_file() -> None:
    os.makedirs(os.path.dirname(WATCHLIST_FILE), exist_ok=True)
    if not os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, "w") as f:
            json.dump([], f)


def load_watchlist() -> List[Dict[str, Any]]:
    _ensure_watchlist_file()
    try:
        with open(WATCHLIST_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        # If file is corrupted or empty, reset it
        with open(WATCHLIST_FILE, "w") as f:
            json.dump([], f)
        return []


def save_watchlist(watchlist: List[Dict[str, Any]]) -> None:
    _ensure_watchlist_file()
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(watchlist, f, indent=2)


def add_movie(movie: Dict[str, Any]) -> bool:
    watchlist = load_watchlist()
    if any(m["id"] == movie["id"] for m in watchlist):
        return False

    watchlist.append(
        {
            "id": movie["id"],
            "title": movie["title"],
            "poster_path": movie["poster_path"],
            "added_at": str(date.today()),
            "watched": False,
        }
    )
    save_watchlist(watchlist)
    return True


def toggle_watched(movie_id: int) -> None:
    watchlist = load_watchlist()
    for item in watchlist:
        if item["id"] == movie_id:
            item["watched"] = not item["watched"]
            break
    save_watchlist(watchlist)


def remove_movie(movie_id: int) -> None:
    watchlist = load_watchlist()
    watchlist[:] = [m for m in watchlist if m["id"] != movie_id]
    save_watchlist(watchlist)
