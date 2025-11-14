"""
The flask application package.
"""

import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# loggign setup
if os.path.exists('logs'):
    pass
else:
    os.mkdir('logs')

log_path = os.path.join('logs', 'flaskapp.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] in %(pathname)s:%(lineno)d - %(message)s'
)

# stream handlet
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_format = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
stream_handler.setFormatter(stream_format)

# app logger
app.logger.addHandler(stream_handler)
app.logger.info('Starting FlaskWebProject')

# session
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
