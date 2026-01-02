from flask import Flask
from app.routes.blog import blog_route

def create_app():
    app = Flask(__name__)

    app.config.update( DEBUG = True, ENV = "development")
    app.register_blueprint(blog_route)

    return app