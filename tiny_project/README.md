# Tiny Project

A simple data analysis project demonstrating data manipulation, database connections,
API clients, and web scraping.

## Project Structure

```bash
tiny_project/
  - data/
    - input/
      - data_file.csv
    - output/
      - results.png
  - db/
    - database_connection.py
  - web/
    - api_client.py
    - web_scraper.py
  - notebooks/
    - analysis.ipynb
  - main.py
  - pyproject.toml
  - README.md
```

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

1. Set up environment variables (if needed):

   ```bash
   export POSTGRES_USER=postgres
   export POSTGRES_PASSWORD=postgres
   export POSTGRES_HOST=localhost
   export POSTGRES_PORT=5400
   export POSTGRES_DB=northwind
   ```

## Usage

Run the main script:

```bash
uv run main.py
```

Or open the notebook:

```bash
uv run jupyter notebook notebooks/analysis.ipynb
```
