import pytest
from app.main.dao.comments_dao import CommentsDAO
from classes.comments import Comments


class TestCommentsDAO:

    def test_get_data(self):
        comments = CommentsDAO()
        assert isinstance(comments.get_data(), list), "Не является списком"
        for comment in comments.get_data():
            assert isinstance(comment, dict), "Один из элементов списка не является словарем"
            assert comment.keys() == {"post_id",
                                      "commenter_name",
                                      "comment",
                                      "pk"}, "Не хватает ключей в одном из словарей"

    def test_get_comments_all(self):
        comments = CommentsDAO()
        assert isinstance(comments.get_comments_all(), list), "Не является списком"
        for comment in comments.get_comments_all():
            assert isinstance(comment, Comments), "Один из элементов списка не является " \
                                                  "экземпляром класса Comments"

    def test_get_comments_by_post_id(self):
        comments = CommentsDAO()
        assert isinstance(comments.get_comments_by_post_id(1), list), "Не является списком"
