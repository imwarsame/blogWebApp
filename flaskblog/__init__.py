# initialising our application and bringing together
# the different components of our webapp
# helps prevent circle-dependency when it comes to imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()  # initialising
bcrypt = Bcrypt()  # initialising
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"  # bootstrap info css in blue
mail = Mail()


# helps creating app for diff envs
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
