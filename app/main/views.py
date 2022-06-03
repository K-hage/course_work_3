from flask import Blueprint, render_template, request, abort

from app.bookmarks.dao.bookmarks_dao import BookmarksDAO
from app.main.dao.post_dao import PostDAO
from app.main.dao.comments_dao import CommentsDAO

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route('/')
def main_page():
    posts = PostDAO().get_post_all()
    bookmarks_count = BookmarksDAO().count_bookmarks()
    return render_template('index.html', posts=posts, bookmarks_count=bookmarks_count)


@main_blueprint.route('/post/<int:post_id>/')
def post_page(post_id):
    post = PostDAO().get_post_by_pk(post_id)
    comments = CommentsDAO().get_comments_by_post_id(post_id)
    post.text_for_tag_link()

    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search/', methods=['GET'])
def search_page():
    posts = ""
    if request.args.get("s"):
        query = request.args.get("s")
        posts = PostDAO().search_for_posts(query)

    return render_template('search.html', posts=posts)


@main_blueprint.route('/user-feeds/<user_name>/')
def user_feeds_page(user_name):
    try:
        posts = PostDAO().get_posts_by_user(user_name)
    except ValueError:
        abort(404)
    else:
        return render_template('user-feed.html', posts=posts)


@main_blueprint.route('/tags/<tag_name>/')
def tag_page(tag_name):
    posts = PostDAO().search_for_tags(tag_name)
    return render_template('tag.html', posts=posts, tag=tag_name)
