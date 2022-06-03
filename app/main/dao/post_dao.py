import json
from classes.post_data import Post
from config import POST_DATA


class PostDAO:

    def __init__(self, path=POST_DATA):
        self.path = path

    def get_data(self):
        """
        Возвращает список постов из json
        """

        with open(self.path, encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_api_post(self, post_id):
        """
        Возвращает словарь поста
        """

        data = self.get_data()
        return next((x for x in data if x['pk'] == post_id), None)

    def get_post_all(self):
        """
        Возвращает список классов постов
        """
        data = self.get_data()
        return [Post(x['poster_name'], x['poster_avatar'], x['pic'],
                     x['content'], x['views_count'], x['likes_count'], x['pk']) for x in data]

    def get_posts_by_user(self, user_name):
        """
        Возвращает список постов по имени
        если нет такого пользователя, то ValueError
        если есть пользователь но нет поста, то пустой список
        """

        data_base = self.get_post_all()
        if next((x for x in data_base if x.poster_name == user_name.lower().strip()), None) is None:
            raise ValueError("Такого пользователя нет")
        return [x for x in data_base if x.poster_name == user_name.lower().strip() and x.content != ""]

    def search_for_posts(self, query):
        """
        Возвращает список постов по ключевому слову
        """

        data_base = self.get_post_all()
        return [x for x in data_base if query.lower().strip() in x.content.lower().strip()]

    def search_for_tags(self, tag_word):
        """
        Возвращает список постов по слову с хештегом
        """

        data_base = self.get_post_all()
        tag = "#" + tag_word.lower().strip()
        return [x for x in data_base if tag in x.content.lower().strip()]

    def get_post_by_pk(self, pk):
        """
        Возвращает пост по порядковому номеру
        """

        data_base = self.get_post_all()
        return next((x for x in data_base if pk == x.pk), None)


# post = PostDAO()
# print(post.search_for_tags("#кот"))
