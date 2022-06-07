import logging
from flask import Blueprint, jsonify
from app.main.dao.post_dao import PostDAO
from config import LOG_PATH

api_blueprint = Blueprint("api_blueprint", __name__)

# создаем логинг доступа к api
log_api = logging.getLogger("api_log")
log_api.setLevel(logging.INFO)
file_handler_log_api = logging.FileHandler(LOG_PATH, encoding="utf-8")
log_api.addHandler(file_handler_log_api)

# Создаем формат логов
formatter_log_api = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler_log_api.setFormatter(formatter_log_api)


@api_blueprint.route('/posts/') # страничка api данных постов (json)
def all_json_posts():

    log_api.info("Запрос /api/posts")
    data = PostDAO().get_data()

    return jsonify(data)


@api_blueprint.route('/posts/<int:post_id>/') # страничка api данных поста по введенному id
def json_post(post_id):

    log_api.info(f"Запрос /api/posts/{post_id}")
    data = PostDAO().get_api_post(post_id)

    return jsonify(data)
