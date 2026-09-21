from werkzeug.security import generate_password_hash, check_password_hash


usuarios = [
    {
        "usuario": "admin",
        "senha": generate_password_hash("1234")
    },
    {
        "usuario": "beatriz",
        "senha": generate_password_hash("12345")
    },
    {
        "usuario": "teste",
        "senha": generate_password_hash("senha")
    }
]


def autenticar_usuario(usuario, senha):

    for user in usuarios:

        if user["usuario"] == usuario:
            if check_password_hash(user["senha"], senha):
                return user

    return None