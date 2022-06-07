import json

from app.main.dao.post_dao import PostDAO
from config import BOOKMARKS_DATA


class BookmarksDAO:
    """Класс для работы с закладками"""

    def __init__(self, path=BOOKMARKS_DATA):
        self.path = path

    def load_data(self):
        """
        Возвращает список id закладок
        """

        with open(self.path, encoding="utf-8") as file:
            return json.load(file)

    def get_post_bookmarks(self):
        """
        Возвращает список классов постов по данным из списка закладок
        """

        data = self.load_data()
        return [PostDAO().get_post_by_pk(i) for i in data]

    def add_dump_data(self, post_id):
        """
        Сохраняет id новой закладки, если такой нет
        """

        data = self.load_data()
        data.append(post_id)
        data = list(set(data))
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def remove_dump_data(self, post_id):
        """
        Удаляет id закладки из списка
        """

        data = self.load_data()
        data.remove(post_id)
        data = list(set(data))
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def count_bookmarks(self):
        """Возвращает количество закладок"""

        return len(self.load_data())


