from app.database import ConnectionManager

class Avaliacao:
    def __init__(self, nota, comentario, livro_id, usuario_id, id=None):
        self.id=id; self.nota=nota; self.comentario=comentario
        self.livro_id=livro_id; self.usuario_id=usuario_id

    def salvar(self):
        with ConnectionManager() as db:
            db.cursor.execute("INSERT INTO avaliacoes (nota, comentario, livro_id, usuario_id) VALUES (?, ?, ?, ?)", (self.nota, self.comentario, self.livro_id, self.usuario_id))
            self.id=db.cursor.lastrowid

    @classmethod
    def listar_por_usuario(cls, usuario_id):
        with ConnectionManager() as db:
            db.cursor.execute("SELECT a.id, a.nota, a.comentario, a.livro_id, a.usuario_id, l.titulo FROM avaliacoes a JOIN livros l ON l.id=a.livro_id WHERE a.usuario_id=? AND l.usuario_id=? ORDER BY a.id DESC", (usuario_id, usuario_id))
            return [dict(r) for r in db.cursor.fetchall()]

    @classmethod
    def excluir(cls, id_avaliacao, usuario_id):
        with ConnectionManager() as db:
            db.cursor.execute("DELETE FROM avaliacoes WHERE id=? AND usuario_id=?", (id_avaliacao, usuario_id))
            return db.cursor.rowcount > 0
