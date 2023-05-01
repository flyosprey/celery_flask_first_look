
from flask import Flask
from project import models
from .extensions import my_celery
from .db import db
from .views import main


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SECRET_KEY"] = "IAMTHEONEWHOKNOCKS"

    my_celery.init_app(app)
    db.init_app(app)

    @app.before_request
    def create_tables():
        db.create_all()

    app.register_blueprint(main)

    return app, my_celery.celery
