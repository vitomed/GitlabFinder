from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from gitlab import Gitlab

app = Flask(__name__)
db = SQLAlchemy()
gl = Gitlab('https://gitlab.com/', private_token='mpFQR4rh6EsP4UyP1wMK')
# migrate = Migrate(app, db)


