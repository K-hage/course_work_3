from flask import Blueprint, render_template, request, redirect

from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


@bookmarks_blueprint.route('/')
def bookmarks_page():
    posts = BookmarksDAO().get_post_bookmarks()
    return render_template("bookmarks.html", posts=posts)


@bookmarks_blueprint.route('/add/<int:post_id>/')
def bookmark_add_page(post_id):
    BookmarksDAO().add_dump_data(post_id)
    return redirect(request.referrer, code=302)


@bookmarks_blueprint.route('/remove/<int:post_id>/')
def bookmark_remove_page(post_id):
    BookmarksDAO().remove_dump_data(post_id)
    return redirect(request.referrer, code=302)
