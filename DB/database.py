import sqlite3
from pathlib import Path
import uuid

from DB.func.usuarios import *
from DB.func.mensagens import *
from DB.func.contatos import *
from DB.func.modelos_mensagem import *


class Database:
    def __init__(self, db_name="config.db"):
        user_dir = Path.home() / "nZap-refac"
        user_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = user_dir / db_name

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._criar_tabelas()

    def _novo_uuid(self):
        """Gera um UUID4 como string."""
        return str(uuid.uuid4())

    def _criar_tabelas(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            numero TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            visivel BOOLEAN DEFAULT 1
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            id_usuario TEXT PRIMARY KEY,
            remetente TEXT NOT NULL,
            hora_inicio TEXT DEFAULT '08:00',
            hora_final TEXT DEFAULT '18:00',
            intervalo_exec INTEGER NOT NULL,
            confirmar_envio BOOLEAN DEFAULT 0,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id) ON DELETE CASCADE
        )
        """)
        self.conn.commit()


        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensagens (
            id TEXT PRIMARY KEY,
            usuario_id TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_envio TEXT,
            visivel BOOLEAN DEFAULT 1,
            enviado BOOLEAN DEFAULT 1,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)  ON DELETE CASCADE
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id TEXT PRIMARY KEY,
            id_usuario TEXT NOT NULL,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            aniversario TEXT,
            vencimento TEXT,
            visivel BOOLEAN DEFAULT 1,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)  ON DELETE CASCADE
        )
        """)
        self.conn.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS modelos_mensagem (
            id TEXT PRIMARY KEY,
            id_usuario TEXT NOT NULL,
            titulo TEXT NOT NULL,
            texto TEXT NOT NULL,
            visivel BOOLEAN DEFAULT 1,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id) ON DELETE CASCADE
        )
        """)
        self.conn.commit()


    # ---------------- CRUD: USUÁRIOS ---------------- #
    criar_usuario = criar_usuario
    ler_usuarios = ler_usuarios
    atualizar_usuario = atualizar_usuario
    deletar_usuario = deletar_usuario
    restaurar_usuario = restaurar_usuario
    deletar_usuario_permanentemente = deletar_usuario_permanentemente

  # ---------------- CRUD: MENSAGENS ---------------- #
    
    criar_modelo_mensagem = criar_modelo_mensagem
    ler_modelos_mensagem = ler_modelos_mensagem
    atualizar_modelo_mensagem = atualizar_modelo_mensagem
    deletar_modelo_mensagem = deletar_modelo_mensagem
    restaurar_modelo_mensagem = restaurar_modelo_mensagem
    deletar_modelo_mensagem_permanentemente = deletar_modelo_mensagem_permanentemente
  # ---------------- CRUD: MENSAGENS ---------------- #

    criar_mensagem = criar_mensagem
    ler_mensagens = ler_mensagens
    atualizar_mensagem = atualizar_mensagem
    deletar_mensagem = deletar_mensagem
    restaurar_mensagem = restaurar_mensagem
    deletar_mensagem_permanentemente = deletar_mensagem_permanentemente

 # ---------------- CRUD: CONTATOS (AGENDA) ---------------- #

    criar_contato = criar_contato
    ler_contatos = ler_contatos
    atualizar_contato = atualizar_contato
    deletar_contato = deletar_contato
    restaurar_contato = restaurar_contato
    deletar_contato_definitivamente = deletar_contato_definitivamente   
 # -------------------------------------- #

    def fechar(self):
        """Fecha a conexão com o banco."""
        self.conn.close()

