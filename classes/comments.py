class Comments:
    """Класс, содержащий комментарии постов"""

    def __init__(self,
                 post_id,
                 commenter_name,
                 comment,
                 pk):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

    def __repr__(self):
        return f"Идентификатор поста: {self.post_id}\n" \
               f"Имя комментатора: {self.commenter_name}\n" \
               f"Комментарий: {self.comment}\n" \
               f"Порядковый номер: {self.pk}\n"

