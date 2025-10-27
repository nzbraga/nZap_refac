import sqlite3


def criar_usuario(self, nome: str, numero: str):
    try:
        novo_id = self._novo_uuid()
        self.cursor.execute(
            "INSERT INTO usuarios (id, nome, numero, visivel) VALUES (?, ?, ?, 1)",
            (novo_id, nome, numero)
        )
        self.conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"[ERRO] O número '{numero}' já existe no banco.")
        return False

def ler_usuarios(self, incluir_ocultos: bool = False, filtro: str = None):
    """Lê usuários (visíveis por padrão)."""
    sql = "SELECT * FROM usuarios WHERE 1=1"
    params = []

    if not incluir_ocultos:
        sql += " AND visivel = 1"

    if filtro:
        sql += " AND (nome LIKE ? OR numero LIKE ?)"
        params.extend((f"%{filtro}%", f"%{filtro}%"))

    self.cursor.execute(sql, params)
    return self.cursor.fetchall()

def atualizar_usuario(self, user_id: int, nome: str = None, numero: str = None):
    """Atualiza um registro de usuário."""
    campos, valores = [], []
    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if numero:
        campos.append("numero = ?")
        valores.append(numero)

    if not campos:
        return False

    valores.append(user_id)
    sql = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True

def deletar_usuario(self, user_id: int):
    """Soft delete: apenas marca o usuário como invisível."""
    self.cursor.execute(
        "UPDATE usuarios SET visivel = 0 WHERE id = ?", (user_id,)
    )
    self.conn.commit()
    return True

def restaurar_usuario(self, user_id: int):
    """Restaura um usuário deletado (visível = 1 novamente)."""
    self.cursor.execute(
        "UPDATE usuarios SET visivel = 1 WHERE id = ?", (user_id,)
    )
    self.conn.commit()
    return True

def deletar_usuario_permanentemente(self, user_id: int):
    self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    self.conn.commit()
