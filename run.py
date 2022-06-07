from flask import Flask

from app.api.views import api_blueprint
from app.bookmarks.views import bookmarks_blueprint
from app.main.views import main_blueprint
from app.errors.views import errors_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # отключаем кодировку api для корректной работы json данных

app.register_blueprint(main_blueprint)  # регистрируем блюпринт главной страницы и поисков
app.register_blueprint(errors_blueprint)  # регистрируем блюпринт с обработчиками ошибок
app.register_blueprint(api_blueprint, url_prefix="/api/")  # регистрируем блюпринт для получения api
app.register_blueprint(bookmarks_blueprint, url_prefix="/bookmarks/")  # регистрируем блюпринт для работы с закладками

if __name__ == "__main__":
    app.run(host="127.0.0.10", port=8080, debug=True)
