from flask import Blueprint, render_template

errors_blueprint = Blueprint("errors_blueprint", __name__, template_folder="templates")


@errors_blueprint.app_errorhandler(404)  # обработчик ошибки 404
def page_not_found(e):
    return render_template('404.html', error=e), 404


@errors_blueprint.app_errorhandler(500)  # обработчик ошибки 500
def server_error(e):
    return render_template('500.html', error=e), 500
