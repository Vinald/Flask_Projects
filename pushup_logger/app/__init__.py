import os
import secrets
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

from app.extensions import db
from app.routes.auth import auth as auth_blueprint
from app.routes.workout import workouts as workout_blueprint
from app.routes.user import user as user_blueprint
from app.models.user import User
from app.models.workout import Workout

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or secrets.token_urlsafe(32)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///db.sqlite3")

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.config.update(DEBUG=True, ENV="development")

    app.register_blueprint(workout_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)

    with app.app_context():
        db.create_all()

    return app