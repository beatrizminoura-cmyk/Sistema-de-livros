from flask import Flask, render_template
from config import Config
from app.controllers import auth_bp, main_bp

def create_app():
    app = Flask(__name__, template_folder="views", static_folder="static")
    app.config.from_object(Config)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def pagina_nao_encontrada(erro):
        app.logger.warning("Página não encontrada: %s", erro)
        return render_template("404.html"), 404

    return app
