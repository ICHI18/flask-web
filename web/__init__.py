from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    UPLOAD_FOLDER = '/Users/super/Desktop/flask-web/web/static'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from . import authors
    app.register_blueprint(authors.bp)

    from . import books
    app.register_blueprint(books.bp)

    app.config.from_mapping(
        SECRET_KRY = 'temp',
        DATABASE = os.path.join(app.instance_path,'bookdb.sqlite3'),
    )

    from . import bookdb
    bookdb.init_app(app)

    return app