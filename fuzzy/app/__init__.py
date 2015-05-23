from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# This import needs to be at the bottom of the file to
# avoid a circular input in views.py
# Views must be contained so that the app can hit routes.
from app import views, models
