# initialising our application and bringing together
# the different components of our webapp
# helps prevent circle-dependency when it comes to imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(
    32
)  # fixes error message "KeyError: 'A secret key is required to use CSRF.'"
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)  # initialising
bcrypt = Bcrypt(app)  # initialising
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"  # bootstrap info css in blue
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASSWORD")
mail = Mail(app)

from flaskblog import (
    routes,
)  # putting it here to avoid another circular import dependency
