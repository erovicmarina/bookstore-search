# Bookstore Search — Knjizevni klub Naravoucenije

A simple search tool for a Serbian book club's lending library, built to replace manually searching through Notion.

## What it does

Volunteers manage the book catalog in Notion. This tool pulls that data through the Notion API and provides a fast, live search page where members can look up books by title or author and instantly see their status (available, borrowed, reserved, etc.).

## Why

The club's Notion database works well for data entry, but isn't fast for quick lookups, especially for members who just want to check if a book is available. This tool solves that with a lightweight search interface.

## Tech stack

- **Backend:** Python, Flask
- **Data source:** Notion API (via `notion-client`)
- **Frontend:** Plain HTML, CSS, JavaScript (no frameworks)
- **Deployment:** Render

## How it works

1. Flask backend (`app.py`) authenticates with the Notion API using a private integration token
2. `/api/books` fetches all books from the Notion database, handling pagination automatically, and returns clean JSON
3. `/search` serves a simple HTML page that fetches this data and provides instant, client-side search filtering by title or author

## Running locally
pip install -r requirements.txt
python app.py

Then visit `http://127.0.0.1:5000/search`

You'll need a `.env` file with:
NOTION_TOKEN=your_notion_integration_token
NOTION_DATASOURCE_ID=your_data_source_id

## Status

Actively used by / built for a local book club as a volunteer project. Planned next steps: status filtering, deployment polish.