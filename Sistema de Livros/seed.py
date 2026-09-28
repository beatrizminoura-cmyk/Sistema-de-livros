from app.database.init_db import inicializar_banco
from app.models import buscar_por_email, criar_usuario

# Cria as tabelas
inicializar_banco()

# Insere usuário de teste apenas se não existir
if not buscar_por_email("beatriz@email.com"):
    criar_usuario(
        "Beatriz",
        "beatriz@email.com",
        "12345"
    )
    print("Usuário criado.")
else:
    print("Usuário já existe.")