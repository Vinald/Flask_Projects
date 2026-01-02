from flask import Flask
from dotenv import load_dotenv
import os
from app.routes.blog import blog_route
from app.routes.auth import auth_route

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config.update(DEBUG=True, ENV="development")
    app.register_blueprint(blog_route)
    app.register_blueprint(auth_route)

    return app
