# Meus Livros — Sistema de gerenciamento de leituras

Aplicação web MPA desenvolvida com Python, Flask, Jinja2 e SQLite3. Permite criar conta, entrar, cadastrar/listar/excluir livros e cadastrar/listar/excluir avaliações vinculadas aos livros.

## Requisitos
- Python 3.10 ou superior

## Instalação e execução
1. Crie e ative um ambiente virtual: `python -m venv .venv`
2. Instale as dependências: `pip install -r requirements.txt`
3. Inicialize o banco e o usuário de teste: `python iniciar_bd.py`
4. Inicie o servidor: `python run.py`
5. Acesse `http://127.0.0.1:5000`

## Credenciais de teste
- E-mail: `teste@livros.com`
- Senha: `123456`

As senhas são armazenadas com hash do Werkzeug. Os registros de livros e avaliações são vinculados ao usuário autenticado.

## Organização
- `app/models`: classes de domínio e comandos SQL parametrizados.
- `app/controllers`: rotas organizadas em Blueprints.
- `app/views`: templates Jinja2.
- `app/middleware`: proteção de rotas.
- `app/database`: conexão SQLite com gerenciador de contexto.
