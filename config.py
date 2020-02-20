import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'projects.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEDUG = True




# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')