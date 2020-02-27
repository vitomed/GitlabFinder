import os
import logging
from logging.handlers import RotatingFileHandler

from app.models import db
from app.routes import app
from config import ConfigApp


app.config.from_object(ConfigApp)
db.init_app(app)
db.create_all(app=app)

if not app.config["TESTING"]:

    if not os.path.exists('log'):
        os.mkdir('log')

    file_handler = RotatingFileHandler('log/gitlab.log',
                                       maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Gitlab API project startup')

app.run(host='0.0.0.0', port=5023)
