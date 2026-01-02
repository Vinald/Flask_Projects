import os
import secrets
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint

load_dotenv()  # loads variables from `./.env` into the environment

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # load from environment with sensible defaults
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or secrets.token_urlsafe(32)
    if not os.getenv("SECRET_KEY"):
        print("Warning: SECRET_KEY not set in .env — generated ephemeral key; add SECRET_KEY to .env for persistence")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///push.db")
    db.init_app(app)

    app.config.update(DEBUG=True, ENV="development")

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app