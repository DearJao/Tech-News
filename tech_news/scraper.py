import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    news_list = selector.css("h2 a::attr(href)").getall()

    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    page_list = selector.css("a.next::attr(href)").get()

    return page_list


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    reading_time = int(
        selector.css("li.meta-reading-time::text").get().split(" ")[0]
    )
    summary = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    )
    category = selector.css("span.label::text").get()

    scrapy_news = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary.strip(),
        "category": category,
    }

    return scrapy_news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []

    while len(news) < amount:
        fetch_news = fetch(url)
        news += scrape_updates(fetch_news)
        url = scrape_next_page_link(fetch_news)

    scrape_each_news = [
        scrape_news(fetch(url)) for url in news[:amount]
    ]

    create_news(scrape_each_news)
    return scrape_each_news
