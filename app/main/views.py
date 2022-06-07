from flask import Blueprint, render_template, request, abort

from app.bookmarks.dao.bookmarks_dao import BookmarksDAO
from app.main.dao.post_dao import PostDAO
from app.main.dao.comments_dao import CommentsDAO

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route('/')  # Главная страница
def main_page():
    posts = PostDAO().get_post_all()
    bookmarks_count = BookmarksDAO().count_bookmarks()
    return render_template('index.html', posts=posts, bookmarks_count=bookmarks_count)


@main_blueprint.route('/post/<int:post_id>/')  # страница постов по id
def post_page(post_id):
    # получаем пост, если поста с таким id нет, то выдаем ошибку 404
    post = PostDAO().get_post_by_pk(post_id)

    if post is None:
        return abort(404)
    comments = CommentsDAO().get_comments_by_post_id(post_id)

    # Преобразовываем хештеги текста в ссылки
    post.text_for_tag_link()

    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search/', methods=['GET'])  # страница поиска
def search_page():
    posts = ""

    # Проверяем полученный запрос, если есть возвращаем список постов
    if request.args.get("s"):
        query = request.args.get("s")
        posts = PostDAO().search_for_posts(query)

    return render_template('search.html', posts=posts)


@main_blueprint.route('/user-feeds/<user_name>/')  # страница поиска постов по имени
def user_feeds_page(user_name):
    # Если пользователя нет, то ошибка значения отправляет в обработчик ошибки 404
    try:
        posts = PostDAO().get_posts_by_user(user_name)
    except ValueError:
        abort(404)
    else:

        return render_template('user-feed.html', posts=posts)


@main_blueprint.route('/tags/<tag_name>/')  # страница поиска по хештегу
def tag_page(tag_name):
    posts = PostDAO().search_for_tags(tag_name)

    return render_template('tag.html', posts=posts, tag=tag_name)
