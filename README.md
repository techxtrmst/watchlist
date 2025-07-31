# 🎬 Movie Watchlist App

A clean and intuitive movie watchlist application built with Streamlit that helps you discover, track, and manage your favorite movies using The Movie Database (TMDB) API.

## ✨ Features

- **🔍 Movie Discovery**: Browse trending, popular, and upcoming movies
- **🔎 Search**: Search movies by title with real-time results
- **📋 Personal Watchlist**: Add movies to your watchlist and track watched status
- **🎭 Detailed Movie Info**: View comprehensive movie details including cast, ratings, genres, and runtime
- **💾 Persistent Storage**: Your watchlist is saved locally and persists between sessions

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web app framework
- **API**: [The Movie Database (TMDB) API](https://www.themoviedb.org/documentation/api) - Movie data and images
- **Data Storage**: JSON file-based local storage
- **HTTP Client**: [Requests](https://requests.readthedocs.io/) - API communication
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

## 📁 Project Structure

```
watchlist/
├── components/             # Reusable UI components
│   ├── card.py             # Movie card component
│   └── filters.py          # Filter input components
├── services/               # Business logic and API integration
│   ├── tmdb.py             # TMDB API service
│   └── watchlist.py        # Watchlist data management
├── views/                  # Page components
│   ├── home.py             # Home page (trending, popular, upcoming)
│   ├── all_shows.py        # Search and browse all movies
│   ├── watchlist.py        # Personal watchlist management
│   └── show_details.py     # Movie details page
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── main.py                 # Main application entry point
├── Pipfile                 # Pipenv dependencies
├── Pipfile.lock            # Pipenv lock file (auto-generated)
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 🚀 Setup and Installation

### Prerequisites

- Python 3.12+
- TMDB API Key (free from [themoviedb.org](https://www.themoviedb.org/settings/api))

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/techxtrmst/watchlist.git
   cd watchlist
   ```

2. **Install dependencies**

   Using Pipenv (recommended):

   ```bash
   pipenv install
   ```

   Or using pip with virtual environment:

   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env and add your TMDB API key
   TMDB_API_KEY=your_api_key_here
   ```

4. **Get your TMDB API Key**
   - Sign up at [The Movie Database](https://www.themoviedb.org/)
   - Go to Settings → API
   - Request an API key (it's free!)
   - Copy the API key to your `.env` file

## 🎮 Running the Application

1. **Activate your virtual environment**:

   ```bash
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. **Run the application**:
   ```bash
   streamlit run main.py
   ```

The app will be available at `http://localhost:8501`