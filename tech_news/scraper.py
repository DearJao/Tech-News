import requests
import time


# Requisito 1
def fetch(url):
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=2)

        if response.status_code != 200:
            raise requests.RequestException

    except (requests.RequestException, requests.ReadTimeout):
        return None
    else:
        return response.text
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
