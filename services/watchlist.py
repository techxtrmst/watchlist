import os
import asyncio
from datetime import date
from tortoise.models import Model
from typing import List, Dict, Any
from tortoise import Tortoise, fields


# Database Model
class WatchlistItem(Model):
    id = fields.IntField(pk=True)
    movie_id = fields.IntField(unique=True)
    title = fields.CharField(max_length=255)
    poster_path = fields.CharField(max_length=255, null=True)
    added_at = fields.DateField()
    watched = fields.BooleanField(default=False)

    class Meta:
        table = "watchlist"


# Database Configuration
DATABASE_URL = "sqlite://data/watchlist.sqlite3"


async def init_db():
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    await Tortoise.init(db_url=DATABASE_URL, modules={"models": [__name__]})
    await Tortoise.generate_schemas()


async def close_db():
    """Close database connection"""
    await Tortoise.close_connections()


def run_async(coro):
    """Helper to run async functions in sync context"""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If loop is already running, create a new task
            import concurrent.futures

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, coro)
                return future.result()
        else:
            return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)


# Async implementations
async def _load_watchlist() -> List[Dict[str, Any]]:
    await init_db()
    try:
        items = await WatchlistItem.all()
        return [
            {
                "id": item.movie_id,
                "title": item.title,
                "poster_path": item.poster_path,
                "added_at": str(item.added_at),
                "watched": item.watched,
            }
            for item in items
        ]
    finally:
        await close_db()


async def _add_movie(movie: Dict[str, Any]) -> bool:
    await init_db()
    try:
        # Check if movie already exists
        existing = await WatchlistItem.filter(movie_id=movie["id"]).first()
        if existing:
            return False

        # Create new watchlist item
        await WatchlistItem.create(
            movie_id=movie["id"],
            title=movie["title"],
            poster_path=movie.get("poster_path"),
            added_at=date.today(),
            watched=False,
        )
        return True
    finally:
        await close_db()


async def _toggle_watched(movie_id: int) -> None:
    await init_db()
    try:
        item = await WatchlistItem.filter(movie_id=movie_id).first()
        if item:
            item.watched = not item.watched
            await item.save()
    finally:
        await close_db()


async def _remove_movie(movie_id: int) -> None:
    await init_db()
    try:
        await WatchlistItem.filter(movie_id=movie_id).delete()
    finally:
        await close_db()


# Synchronous interfaces
def load_watchlist() -> List[Dict[str, Any]]:
    """Load all watchlist items"""
    return run_async(_load_watchlist())


def add_movie(movie: Dict[str, Any]) -> bool:
    """Add a movie to the watchlist. Returns True if added, False if already exists."""
    return run_async(_add_movie(movie))


def toggle_watched(movie_id: int) -> None:
    """Toggle the watched status of a movie"""
    run_async(_toggle_watched(movie_id))


def remove_movie(movie_id: int) -> None:
    """Remove a movie from the watchlist"""
    run_async(_remove_movie(movie_id))
