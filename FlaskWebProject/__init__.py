"""
The flask application package.
"""

import os
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Use Azure-friendly log path
LOG_DIR = os.path.join('/home', 'logs')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, 'flaskapp.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] in %(pathname)s:%(lineno)d - %(message)s'
)

# Stream handler (outputs to container logs / App Service Log Stream)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_format = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
stream_handler.setFormatter(stream_format)
app.logger.addHandler(stream_handler)

app.logger.info("Flask app started on Azure App Service")

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
