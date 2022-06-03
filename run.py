from flask import Flask

from app.api.views import api_blueprint
from app.bookmarks.views import bookmarks_blueprint
from app.main.views import main_blueprint
from app.errors.views import errors_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(errors_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api/")
app.register_blueprint(bookmarks_blueprint, url_prefix="/bookmarks/")

if __name__ == "__main__":
    app.run(host="127.0.0.10", port=8080, debug=True)
