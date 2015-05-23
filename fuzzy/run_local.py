# Running a dev server
import os
os.environ['APP_SETTINGS'] = 'config.DevConfig'

# Run server
from app import app
app.run(host='127.0.0.1', port=5100, debug=True)
