
def criar_mensagem(self, usuario_id: str, conteudo: str, data_envio: str):
    novo_id = self._novo_uuid()
    self.cursor.execute(
        "INSERT INTO mensagens (id, usuario_id, conteudo, data_envio) VALUES (?, ?, ?, ?)",
        (novo_id, usuario_id, conteudo, data_envio)
    )
    self.conn.commit()

def atualizar_mensagem(self, message_id: str, conteudo: str = None, data_envio: str = None):
    """Atualiza os dados de uma mensagem."""
    campos, valores = [], []

    if conteudo is not None:
        campos.append("conteudo = ?")
        valores.append(conteudo)
    if data_envio is not None:
        campos.append("data_envio = ?")
        valores.append(data_envio)

    if not campos:
        return False  # nada para atualizar

    valores.append(message_id)
    sql = f"UPDATE mensagens SET {', '.join(campos)} WHERE id = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True


def deletar_mensagem(self, message_id: int):
    """Soft delete: apenas marca a mensagem como invisível."""
    self.cursor.execute(
        "UPDATE mensagens SET visivel = 0 WHERE id = ?", (message_id,)
    )
    self.conn.commit()
    return True
# Ler mensagens (opcional incluir ocultas)
def ler_mensagens(self, usuario_id: int, incluir_ocultos: bool = False):
    """Lê todas as mensagens de um usuário."""
    sql = "SELECT * FROM mensagens WHERE usuario_id = ?"
    params = [usuario_id]

    if not incluir_ocultos:
        sql += " AND visivel = 1"

    self.cursor.execute(sql, params)
    return self.cursor.fetchall()
# Restaurar mensagem
def restaurar_mensagem(self, message_id: int):
    """Restaura uma mensagem deletada."""
    self.cursor.execute(
        "UPDATE mensagens SET visivel = 1 WHERE id = ?", (message_id,)
    )
    self.conn.commit()
    return True

def deletar_mensagem_permanentemente(self, message_id: int):
    self.cursor.execute("DELETE FROM mensagens WHERE id = ?", (message_id,))
    self.conn.commit()
