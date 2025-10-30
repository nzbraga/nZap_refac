# Criar modelo de mensagem
def criar_modelo_mensagem(self, id_usuario: str, titulo: str, texto: str):
    """Cria um novo modelo de mensagem."""
    novo_id = self._novo_uuid()
    self.cursor.execute(
        "INSERT INTO modelos_mensagem (id, id_usuario, titulo, texto, visivel) VALUES (?, ?, ?, ?, ?)",
        (novo_id, id_usuario, titulo, texto, 1)
    )
    self.conn.commit()
    return novo_id


# Atualizar modelo de mensagem
def atualizar_modelo_mensagem(self, modelo_id: str, titulo: str = None, texto: str = None):
    """Atualiza os dados de um modelo de mensagem."""
    campos, valores = [], []

    if titulo is not None:
        campos.append("titulo = ?")
        valores.append(titulo)
    if texto is not None:
        campos.append("texto = ?")
        valores.append(texto)

    if not campos:
        return False  # nada para atualizar

    valores.append(modelo_id)
    sql = f"UPDATE modelos_mensagem SET {', '.join(campos)} WHERE id = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True


# Soft delete
def deletar_modelo_mensagem(self, modelo_id: str):
    """Soft delete: apenas marca o modelo como invisível."""
    self.cursor.execute(
        "UPDATE modelos_mensagem SET visivel = 0 WHERE id = ?", (modelo_id,)
    )
    self.conn.commit()
    return True


# Ler modelos de mensagem
def ler_modelos_mensagem(self, id_usuario: str, incluir_ocultos: bool = False):
    """Lê todos os modelos de um usuário."""
    sql = "SELECT * FROM modelos_mensagem WHERE id_usuario = ?"
    params = [id_usuario]

    if not incluir_ocultos:
        sql += " AND visivel = 1"

    self.cursor.execute(sql, params)
    return self.cursor.fetchall()


# Restaurar modelo de mensagem
def restaurar_modelo_mensagem(self, modelo_id: str):
    """Restaura um modelo de mensagem deletado."""
    self.cursor.execute(
        "UPDATE modelos_mensagem SET visivel = 1 WHERE id = ?", (modelo_id,)
    )
    self.conn.commit()
    return True


# Deletar modelo permanentemente
def deletar_modelo_mensagem_permanentemente(self, modelo_id: str):
    """Remove definitivamente o modelo do banco."""
    self.cursor.execute("DELETE FROM modelos_mensagem WHERE id = ?", (modelo_id,))
    self.conn.commit()
    return True
