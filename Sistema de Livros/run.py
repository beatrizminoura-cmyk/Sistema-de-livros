from app import create_app
from app.database.init_db import inicializar_banco


app = create_app()


if __name__ == "__main__":

    inicializar_banco()

    app.run(
        debug=True
    )