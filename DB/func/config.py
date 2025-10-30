# Criar configuração
def criar_config(self, id_usuario: str, remetente: str, hora_inicio: str = "08:00",
                 hora_final: str = "18:00", intervalo_exec: int = 60, confirmar_envio: bool = False):
    """Cria uma nova configuração para o usuário."""
    self.cursor.execute(
        """
        INSERT INTO config (id_usuario, remetente, hora_inicio, hora_final, intervalo_exec, confirmar_envio)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (id_usuario, remetente, hora_inicio, hora_final, intervalo_exec, int(confirmar_envio))
    )
    self.conn.commit()
    return True


# Ler configuração
def ler_config(self, id_usuario: str):
    """Lê a configuração de um usuário."""
    self.cursor.execute("SELECT * FROM config WHERE id_usuario = ?", (id_usuario,))
    return self.cursor.fetchone()


# Atualizar configuração
def atualizar_config(self, id_usuario: str, remetente: str = None, hora_inicio: str = None, hora_final: str = None,
                     intervalo_exec: int = None, confirmar_envio: bool = None):
    """Atualiza os campos da configuração do usuário."""
    campos, valores = [], []

    if remetente is not None:
        campos.append("remetente = ?")
        valores.append(remetente)
    if hora_inicio is not None:
        campos.append("hora_inicio = ?")
        valores.append(hora_inicio)
    if hora_final is not None:
        campos.append("hora_final = ?")
        valores.append(hora_final)
    if intervalo_exec is not None:
        campos.append("intervalo_exec = ?")
        valores.append(intervalo_exec)
    if confirmar_envio is not None:
        campos.append("confirmar_envio = ?")
        valores.append(int(confirmar_envio))

    if not campos:
        return False  # nada para atualizar

    valores.append(id_usuario)
    sql = f"UPDATE config SET {', '.join(campos)} WHERE id_usuario = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True


# Deletar configuração (soft delete não se aplica aqui, pois é apenas uma por usuário)
def deletar_config(self, id_usuario: str):
    """Remove permanentemente a configuração do usuário."""
    self.cursor.execute("DELETE FROM config WHERE id_usuario = ?", (id_usuario,))
    self.conn.commit()
    return True
