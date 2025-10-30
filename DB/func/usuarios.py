import sqlite3

# -------------------- USUÁRIOS -------------------- #

def criar_usuario(self, nome: str, numero: str, email: str):
    """Cria um novo usuário com UUID automático."""
    try:
        novo_id = self._novo_uuid()
        self.cursor.execute(
            "INSERT INTO usuarios (id, nome, numero, email, visivel) VALUES (?, ?, ?, ?, 1)",
            (novo_id, nome, numero, email)
        )
        self.conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed: usuarios.numero" in str(e):
            print(f"[ERRO] O número '{numero}' já existe no banco.")
        elif "UNIQUE constraint failed: usuarios.email" in str(e):
            print(f"[ERRO] O email '{email}' já existe no banco.")
        else:
            print(f"[ERRO] {e}")
        return False

def ler_usuarios(self, incluir_ocultos: bool = False, filtro: str = None):
    """Lê usuários (visíveis por padrão)."""
    sql = "SELECT * FROM usuarios WHERE 1=1"
    params = []

    if not incluir_ocultos:
        sql += " AND visivel = 1"

    if filtro:
        sql += " AND (nome LIKE ? OR numero LIKE ? OR email LIKE ?)"
        params.extend((f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))

    self.cursor.execute(sql, params)
    return self.cursor.fetchall()

def atualizar_usuario(self, user_id: str, nome: str = None, numero: str = None, email: str = None):
    """Atualiza um registro de usuário."""
    campos, valores = [], []
    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if numero:
        campos.append("numero = ?")
        valores.append(numero)
    if email:
        campos.append("email = ?")
        valores.append(email)

    if not campos:
        return False

    valores.append(user_id)
    sql = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True

def deletar_usuario(self, user_id: str):
    """Soft delete: apenas marca o usuário como invisível."""
    self.cursor.execute(
        "UPDATE usuarios SET visivel = 0 WHERE id = ?", (user_id,)
    )
    self.conn.commit()
    return True

def restaurar_usuario(self, user_id: str):
    """Restaura um usuário deletado (visível = 1 novamente)."""
    self.cursor.execute(
        "UPDATE usuarios SET visivel = 1 WHERE id = ?", (user_id,)
    )
    self.conn.commit()
    return True

def deletar_usuario_permanentemente(self, user_id: str):
    """Deleta o usuário do banco permanentemente."""
    self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    self.conn.commit()
    return True
