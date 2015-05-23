from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import imp
from migrate.versioning import api
from app import app, db

uri = app.config.get('SQLALCHEMY_DATABASE_URI')
db_repo = app.config.get('SQLALCHEMY_MIGRATE_REPO')

v = api.db_version(uri, db_repo)
migration = db_repo + ('/versions/%03d_migration.py' % (v+1))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(uri, db_repo)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(uri, db_repo, tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(uri, db_repo)
v = api.db_version(uri, db_repo)
print('New migration saved as {}'.format(migration))
print('Current database version: {}'.format(v))
