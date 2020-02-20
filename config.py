import os

basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigApp:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'projects.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEDUG = True


class ConfigTest:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEDUG = True
    TESTING = True

