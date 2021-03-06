from .models import Article

import json
from django.core.serializers.json import DjangoJSONEncoder


def articles_to_news_json(articles: list):
    news = []
    for article in articles:
        news_dict = article_to_news_dict(article)
        news.append(news_dict)
    return json.dumps(news, ensure_ascii=False, cls=DjangoJSONEncoder)


def article_to_news_json(article: Article):
    news_dict = article_to_news_dict(article)
    return json.dumps(news_dict, ensure_ascii=False, cls=DjangoJSONEncoder)


def article_to_news_dict(article: Article):
    if article is None:
        return {}
    return {
        'id': article.id,
        'heading': article.title,
        'thumbnail': article.thumbnail or article.source.image,
        'description': article.content_short,
        'text': '',
        'link': article.link,
        'date': article.date,
        'views_count': 0,
        'likes_count': 0,
        'dislikes_count': 0,
    }
