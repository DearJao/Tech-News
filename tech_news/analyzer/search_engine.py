from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    cursor = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(doc["title"], doc["url"]) for doc in cursor]


# Requisito 8
def search_by_date(date):
    try:
        check_date_format = datetime.fromisoformat(date)
        correct_date = check_date_format.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    news_collection = db.news

    result = news_collection.find(
        {"timestamp": correct_date},
        {
            "_id": 0,
            "title": 1,
            "url": 1,
        },
    )

    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    cursor = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(doc["title"], doc["url"]) for doc in cursor]
