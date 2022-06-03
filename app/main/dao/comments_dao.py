import json
from classes.comments import Comments
from config import COMMENTS_DATA


class CommentsDAO:

    def __init__(self, path=COMMENTS_DATA):
        self.path = path

    def get_data(self):
        """
        Возвращает список словарей комментариев из json
        """

        with open(self.path, encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_comments_all(self):
        """
        Возвращает список классов комментариев
        """

        data = self.get_data()
        return [Comments(x["post_id"], x["commenter_name"], x["comment"], x["pk"]) for x in data]

    def get_comments_by_post_id(self, post_id):
        """
        Возвращает список комментариев по id поста
        """

        data_base = self.get_comments_all()
        return [x for x in data_base if post_id == x.post_id and x.comment != ""]


# comments = CommentsDAO()
# print(comments.get_comments_by_post_id(7))
