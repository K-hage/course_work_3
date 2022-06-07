import pytest
from app.main.dao.post_dao import PostDAO
from classes.post_data import Post


class TestPostDAO:

    def test_get_data(self):
        posts = PostDAO()
        assert isinstance(posts.get_data(), list), "Не является списком"
        for post in posts.get_data():
            assert post.keys() == {"poster_name",
                                   "poster_avatar",
                                   "pic",
                                   "content",
                                   "views_count",
                                   "likes_count",
                                   "pk"}, "Нет нужного ключа в одном из словарей"

    def test_get_api_post(self):
        posts = PostDAO()
        assert isinstance(posts.get_api_post(1), dict)
        assert posts.get_api_post(1).keys() == {"poster_name",
                                                "poster_avatar",
                                                "pic",
                                                "content",
                                                "views_count",
                                                "likes_count",
                                                "pk"}, "Не хватает ключей"

    def test_get_post_all(self):
        posts = PostDAO()
        assert isinstance(posts.get_post_all(), list)

    def test_get_post_by_user(self):
        posts = PostDAO()
        assert isinstance(posts.get_posts_by_user("leo"), list), "Не является списком"
        with pytest.raises(ValueError):
            posts.get_posts_by_user("")

    def test_search_for_posts(self):
        posts = PostDAO()
        assert isinstance(posts.search_for_posts("в"), list), "Не является списком"

    def test_search_for_tags(self):
        posts = PostDAO()
        assert isinstance(posts.search_for_tags("кот"), list), "Не является списком"

    def test_get_post_by_pk(self):
        posts = PostDAO()
        assert isinstance(posts.get_post_by_pk(1), Post), "Не является классом Post"
