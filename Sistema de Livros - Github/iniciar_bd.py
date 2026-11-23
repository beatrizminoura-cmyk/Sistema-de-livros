from app.database.init_db import inicializar_banco
from app.models import Usuario

if __name__ == "__main__":
    inicializar_banco()
    email = "teste@livros.com"
    if Usuario.buscar_por_email(email) is None:
        Usuario(nome="Usuário Teste", email=email, senha="123456").salvar()
    print("Usuário de teste: teste@livros.com | Senha: 123456")
