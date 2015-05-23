# flask config
# define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DEBUG = False
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 2
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True
    CSRF_ENABLED = True
    # Use a secure, unique and absolutely secret key for
    # signing the data. 
    CSRF_SESSION_KEY = "secret"
    # Secret key for signing cookies
    SECRET_KEY = "secret"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository') 

class ProdConfig(Config):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/app'

class StagingConfig(Config):

    DEVELOPMENT = True
    DEBUG = False

class DevConfig(Config):

    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

class TestingConfig(Config):

    TESTING = True

