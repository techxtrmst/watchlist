import json
from typing import List, Dict, Any


WATCHLIST_FILE = "data/watchlist.json"


def load_watchlist() -> List[Dict[str, Any]]:
    with open(WATCHLIST_FILE, "r") as f:
        return json.load(f)


def save_watchlist(watchlist: List[Dict[str, Any]]) -> None:
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(watchlist, f, indent=2)


def add_movie(movie: Dict[str, Any]) -> bool:
    watchlist = load_watchlist()
    if any(m["id"] == movie["id"] for m in watchlist):
        return False  # Already exists
    watchlist.append(
        {
            "id": movie["id"],
            "title": movie["title"],
            "poster_path": movie["poster_path"],
            "added_at": str(__import__("datetime").date.today()),
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
