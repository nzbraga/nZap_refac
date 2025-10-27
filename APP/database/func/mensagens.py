def criar_mensagem(self, usuario_id: str, conteudo: str, data_envio: str, enviado: bool = False):
    """Cria uma nova mensagem para o usuário."""
    novo_id = self._novo_uuid()
    self.cursor.execute(
        "INSERT INTO mensagens (id, usuario_id, conteudo, data_envio, visivel, enviado) VALUES (?, ?, ?, ?, ?, ?)",
        (novo_id, usuario_id, conteudo, data_envio, 1, int(enviado))
    )
    self.conn.commit()
    return novo_id
 # Retorna o ID gerado da mensagem

def atualizar_mensagem(self, message_id: str, conteudo: str = None, data_envio: str = None, enviado: bool = None):
    """Atualiza os dados de uma mensagem."""
    campos, valores = [], []

    if conteudo is not None:
        campos.append("conteudo = ?")
        valores.append(conteudo)
    if data_envio is not None:
        campos.append("data_envio = ?")
        valores.append(data_envio)
    if enviado is not None:
        campos.append("enviado = ?")
        valores.append(int(enviado))

    if not campos:
        return False  # nada para atualizar

    valores.append(message_id)
    sql = f"UPDATE mensagens SET {', '.join(campos)} WHERE id = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True

def deletar_mensagem(self, message_id: str):
    """Soft delete: apenas marca a mensagem como invisível."""
    self.cursor.execute(
        "UPDATE mensagens SET visivel = 0 WHERE id = ?", (message_id,)
    )
    self.conn.commit()
    return True

def ler_mensagens(self, usuario_id: str, incluir_ocultos: bool = False):
    """Lê todas as mensagens de um usuário."""
    sql = "SELECT * FROM mensagens WHERE usuario_id = ?"
    params = [usuario_id]

    if not incluir_ocultos:
        sql += " AND visivel = 1"

    self.cursor.execute(sql, params)
    return self.cursor.fetchall()

def restaurar_mensagem(self, message_id: str):
    """Restaura uma mensagem deletada."""
    self.cursor.execute(
        "UPDATE mensagens SET visivel = 1 WHERE id = ?", (message_id,)
    )
    self.conn.commit()
    return True

def deletar_mensagem_permanentemente(self, message_id: str):
    """Remove definitivamente a mensagem do banco."""
    self.cursor.execute("DELETE FROM mensagens WHERE id = ?", (message_id,))
    self.conn.commit()
    return True
