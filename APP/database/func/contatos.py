def criar_contato(self, id_usuario: str, nome: str, telefone: str,
                    aniversario: str = None, vencimento: str = None):
    novo_id = self._novo_uuid()
    self.cursor.execute("""
        INSERT INTO contatos (id, id_usuario, nome, telefone, aniversario, vencimento, visivel)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    """, (novo_id, id_usuario, nome, telefone, aniversario, vencimento))
    self.conn.commit()

def ler_contatos(self, id_usuario: int, incluir_ocultos: bool = False, filtro: str = None):
    """Lê os contatos de um usuário (visíveis por padrão)."""
    sql = "SELECT * FROM contatos WHERE id_usuario = ?"
    params = [id_usuario]

    if not incluir_ocultos:
        sql += " AND visivel = 1"

    if filtro:
        sql += " AND (nome LIKE ? OR telefone LIKE ?)"
        params.extend((f"%{filtro}%", f"%{filtro}%"))

    self.cursor.execute(sql, params)
    return self.cursor.fetchall()

def atualizar_contato(self, contact_id: int, **kwargs):
    """Atualiza dados de um contato."""
    campos = []
    valores = []
    for campo, valor in kwargs.items():
        campos.append(f"{campo} = ?")
        valores.append(valor)
    if not campos:
        return False

    valores.append(contact_id)
    sql = f"UPDATE contatos SET {', '.join(campos)} WHERE id = ?"
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return True

def deletar_contato(self, contact_id: int):
    """Soft delete: apenas marca o contato como invisível."""
    self.cursor.execute(
        "UPDATE contatos SET visivel = 0 WHERE id = ?", (contact_id,)
    )
    self.conn.commit()
    return True

def restaurar_contato(self, contact_id: int):
    """Restaura um contato deletado."""
    self.cursor.execute(
        "UPDATE contatos SET visivel = 1 WHERE id = ?", (contact_id,)
    )
    self.conn.commit()
    return True

def deletar_contato_definitivamente(self, contact_id: int): 
    self.cursor.execute("DELETE FROM contatos WHERE id = ?", (contact_id,))
    self.conn.commit()
