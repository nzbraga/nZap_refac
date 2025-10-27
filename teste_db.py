from APP.database.database import Database

def testar_database():
    db = Database()

    print("=== TESTE DE USUÁRIOS ===")
    # Criar usuário
    sucesso = db.criar_usuario("João Silva", "11999999999", "joao@email.com")
    print("Criar usuário:", sucesso)

    # Ler usuários
    usuarios = db.ler_usuarios()
    print("Usuários:", usuarios)

    user_id = usuarios[0][0]  # pegar id do primeiro usuário

    # Atualizar usuário
    db.atualizar_usuario(user_id, nome="João S.", numero="11988888888")
    print("Usuário atualizado:", db.ler_usuarios())

    # Soft delete e restaurar
    db.deletar_usuario(user_id)
    print("Após soft delete:", db.ler_usuarios())
    db.restaurar_usuario(user_id)
    print("Após restaurar:", db.ler_usuarios())

    # Deletar permanentemente
    db.deletar_usuario_permanentemente(user_id)
    print("Após exclusão permanente:", db.ler_usuarios())

    print("\n=== TESTE DE MODELOS DE MENSAGEM ===")
    # Criar usuário novamente para testes de mensagens
    db.criar_usuario("Maria", "11977777777", "maria@email.com")
    user_id = db.ler_usuarios()[0][0]

    # Criar modelo
    modelo_id = db.criar_modelo_mensagem(user_id, "Promoção", "Confira nossas promoções!")
    print("Modelo criado:", db.ler_modelos_mensagem(user_id))

    # Atualizar modelo
    db.atualizar_modelo_mensagem(modelo_id, texto="Promoção imperdível!")
    print("Modelo atualizado:", db.ler_modelos_mensagem(user_id))

    # Soft delete e restaurar modelo
    db.deletar_modelo_mensagem(modelo_id)
    print("Após soft delete:", db.ler_modelos_mensagem(user_id))
    db.restaurar_modelo_mensagem(modelo_id)
    print("Após restaurar:", db.ler_modelos_mensagem(user_id))

    # Excluir permanentemente
    db.deletar_modelo_mensagem_permanentemente(modelo_id)
    print("Após exclusão permanente:", db.ler_modelos_mensagem(user_id))

    print("\n=== TESTE DE MENSAGENS ===")
    # Criar mensagem
    msg_id = db.criar_mensagem(user_id, "Olá, teste!", "2025-10-27 16:00", enviado=True)
    print("Mensagem criada:", db.ler_mensagens(user_id))

    # Atualizar mensagem
    db.atualizar_mensagem(msg_id, conteudo="Olá, teste atualizado!")
    print("Mensagem atualizada:", db.ler_mensagens(user_id))

    # Soft delete e restaurar
    db.deletar_mensagem(msg_id)
    print("Após soft delete:", db.ler_mensagens(user_id))
    db.restaurar_mensagem(msg_id)
    print("Após restaurar:", db.ler_mensagens(user_id))

    # Excluir permanentemente
    db.deletar_mensagem_permanentemente(msg_id)
    print("Após exclusão permanente:", db.ler_mensagens(user_id))

    print("\n=== TESTE DE CONTATOS ===")
    # Criar contato
    contato_id = db.criar_contato(user_id, "Carlos", "11966666666", "1990-01-01", "2025-12-31")
    contatos = db.ler_contatos(user_id)
    print("Contato criado:", contatos)

    # Atualizar contato
    db.atualizar_contato(contatos[0][0], nome="Carlos S.", telefone="11955555555")
    print("Contato atualizado:", db.ler_contatos(user_id))

    # Soft delete e restaurar
    db.deletar_contato(contatos[0][0])
    print("Após soft delete:", db.ler_contatos(user_id))
    db.restaurar_contato(contatos[0][0])
    print("Após restaurar:", db.ler_contatos(user_id))

    # Excluir permanentemente
    db.deletar_contato_definitivamente(contatos[0][0])
    print("Após exclusão permanente:", db.ler_contatos(user_id))

    db.fechar()
    print("\n=== TESTE CONCLUÍDO ===")

if __name__ == "__main__":
    testar_database()
