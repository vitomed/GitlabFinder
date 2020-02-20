import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from gitlab import Gitlab

from config import ConfigApp

db = SQLAlchemy()
gl = Gitlab('https://gitlab.com/', private_token='mpFQR4rh6EsP4UyP1wMK')


def create_app(config: object):
    app = Flask(__name__)
    app.config.from_object(config)

    from app.models import db
    db.init_app(app)
    return app


app = create_app(ConfigApp)
db.create_all(app=app)

# migrate = Migrate(app, db)

from app import routes


if not app.debug:

    if not os.path.exists('log'):
        os.mkdir('log')

    file_handler = RotatingFileHandler('log/gitlab.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Gitlab API project startup')
