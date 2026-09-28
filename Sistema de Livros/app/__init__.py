from flask import Flask

from config import Config
from app.controllers import auth_bp, main_bp


def create_app():

    app = Flask(
        __name__,
        template_folder="views",
        static_folder="static"
    )

    app.config.from_object(Config)


    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app