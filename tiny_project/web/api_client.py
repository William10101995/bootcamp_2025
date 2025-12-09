import requests


def get_json_data(url):
    """
    Simple API client to get JSON data from an API endpoint.

    Args:
        url: API endpoint URL

    Returns:
        dict: JSON data from the API
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
