class Post:
    """Класс для хранения поста"""

    def __init__(self,
                 poster_name,
                 poster_avatar,
                 pic,
                 content,
                 views_count,
                 likes_count,
                 pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f"Имя постера: {self.poster_name}\n" \
               f"Ссылка на аватар: {self.poster_avatar}\n" \
               f"Ссылка на картинку: {self.pic}\n" \
               f"Пост: {self.content}" \
               f"Количество просмотров: {self.views_count}\n" \
               f"Количество лайков: {self.likes_count}\n" \
               f"Порядковый номер: {self.pk}"

    def text_for_tag_link(self):
        """
        Преобразует хештеги текста поста в ссылки
        """

        new_text = ""
        for word in self.content.split():
            if '#' == word[0]:
                new_text += f'<a href="/tags/{word[1:]}/">{word}</a> '
            else:
                new_text += f'{word} '
        self.content = new_text
