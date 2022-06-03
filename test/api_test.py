import pytest
from run import app


def test_all_post_app():
    response = app.test_client().get('/api/posts/')
    assert isinstance(response.json, list), 'Неверный тип данных'
    for i in range(len(response.json)):
        assert response.json[i].keys() == {"poster_name",
                                           "poster_avatar",
                                           "pic",
                                           "content",
                                           "views_count",
                                           "likes_count",
                                           "pk"}, "Нет нужного ключа в одном из словарей"


def test_one_post_app():
    response = app.test_client().get('/api/posts/1', follow_redirects=True)
    assert isinstance(response.json, dict), 'Неверный тип данных'
    assert response.json.keys() == {"poster_name",
                                    "poster_avatar",
                                    "pic",
                                    "content",
                                    "views_count",
                                    "likes_count",
                                    "pk"}, "Не хватает ключей"
