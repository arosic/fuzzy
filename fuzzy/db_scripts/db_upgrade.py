#!/flask/bin/python
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from migrate.versioning import api
from app import app

uri = app.config.get('SQLALCHEMY_DATABASE_URI')
db_repo = app.config.get('SQLALCHEMY_MIGRATE_REPO')

api.upgrade(uri, db_repo)
v = api.db_version(uri, db_repo)
print('Current database version: {}'.format(str(v)))
