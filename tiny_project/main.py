import pandas as pd
from db.database_connection import get_engine
from web.api_client import get_json_data
from web.web_scraper import get_html_data
import subprocess
import os


def main():
    """
    Main function that:
    - Gets database engine and reads data with pd.read_sql
    - Uses api_client to get JSON data
    - Uses web_scraper to get HTML data
    - Runs the analysis notebook
    """

    # Get database engine
    engine = get_engine()

    # Example: Read data from database
    try:
        query = "SELECT * FROM customers LIMIT 5"
        df_db = pd.read_sql(query, engine)
        print("Database data:")
        print(df_db.head())
    except Exception as e:
        print(f"Database query failed: {e}")

    # Example: Get JSON data from API
    try:
        api_url = "https://jsonplaceholder.typicode.com/posts/1"
        json_data = get_json_data(api_url)
        print("\nAPI data:")
        print(json_data)
    except Exception as e:
        print(f"API request failed: {e}")

    # Example: Get HTML data from web
    try:
        web_url = "https://example.com"
        html_data = get_html_data(web_url)
        print("\nHTML data (first 200 chars):")
        print(html_data[:200])
    except Exception as e:
        print(f"Web scraping failed: {e}")

    # Run the analysis notebook
    notebook_path = os.path.join("notebooks", "analysis.ipynb")
    if os.path.exists(notebook_path):
        print("\nRunning analysis notebook...")
        try:
            subprocess.run(
                [
                    "jupyter",
                    "nbconvert",
                    "--to",
                    "notebook",
                    "--execute",
                    notebook_path,
                ],
                check=True,
            )
            print("Notebook executed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Notebook execution failed: {e}")
        except FileNotFoundError:
            print("Jupyter nbconvert not found. Please install jupyter and nbconvert.")
    else:
        print(f"Notebook not found at {notebook_path}")


if __name__ == "__main__":
    main()
