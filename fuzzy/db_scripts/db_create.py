#!flask/bin/python
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from migrate.versioning import api
from app import app, db
import os.path

uri = app.config.get('SQLALCHEMY_DATABASE_URI')
repo = app.config.get('SQLALCHEMY_MIGRATE_REPO')
db.create_all()

if not os.path.exists(repo):
	api.create(repo, 'database_repository')
	api.version_control(uri, repo)
else:
	api.version_control(uri, repo, api.version(repo))
