import requests
from bs4 import BeautifulSoup


def get_html_data(url):
    """
    Simple web scraper to get HTML data from a web page.

    Args:
        url: Web page URL

    Returns:
        str: HTML content of the page
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_html(html):
    """
    Parse HTML content using BeautifulSoup.

    Args:
        html: HTML content as string

    Returns:
        BeautifulSoup: Parsed HTML object
    """
    return BeautifulSoup(html, "html.parser")
