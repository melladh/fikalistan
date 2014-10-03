class Configuration(object):
    SECRET_KEY = 'flask-session-insecure-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/fikalistan.db'
    SQLALCHEMY_ECHO = True
    WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'
    DEBUG = True