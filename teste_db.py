from APP.database.database import Database # ajuste o import conforme a localização do seu arquivo

def main():
    db = Database("test_config.db")

    print("===== TESTANDO USUÁRIOS =====")
    # Criar usuários
    db.criar_usuario("Alice", "1111-1111")
    db.criar_usuario("Bob", "2222-2222")
    
    # Ler usuários
    print("Usuários:", db.ler_usuarios())

    # Atualizar usuário
    db.atualizar_usuario(1, nome="Alice Silva")
    print("Usuários após update:", db.ler_usuarios())

    # Deletar usuário
    db.deletar_usuario(2)
    print("Usuários após delete (soft):", db.ler_usuarios())
    print("Incluindo ocultos:", db.ler_usuarios(incluir_ocultos=True))

    # Restaurar usuário
    db.restaurar_usuario(2)
    print("Usuários após restaurar:", db.ler_usuarios())

    print("\n===== TESTANDO MENSAGENS =====")
    # Criar mensagens
    #db.criar_mensagem(1, "Olá, esta é a primeira mensagem!", "2025-10-26 04:00")
    #db.criar_mensagem(1, "Segunda mensagem", "2025-10-26 05:00")
    
    # Ler mensagens
    print("Mensagens do usuário 1:", db.ler_mensagens(1))

    # Deletar mensagem
    db.deletar_mensagem(1)
    print("Mensagens após delete (soft):", db.ler_mensagens(1))
    print("Incluindo ocultas:", db.ler_mensagens(1, incluir_ocultos=True))

    # Restaurar mensagem
    db.restaurar_mensagem(1)
    print("Mensagens após restaurar:", db.ler_mensagens(1))

    print("\n===== TESTANDO CONTATOS =====")
    # Criar contatos
    db.criar_contato(1, "Carol", "3333-3333", aniversario="1990-01-01")
    db.criar_contato(1, "Daniel", "4444-4444")

    # Ler contatos
    print("Contatos do usuário 1:", db.ler_contatos(1))

    # Atualizar contato
    db.atualizar_contato(1, nome="Carol Souza", telefone="3333-0000")
    print("Contatos após update:", db.ler_contatos(1))

    # Deletar contato
    db.deletar_contato(2)
    print("Contatos após delete (soft):", db.ler_contatos(1))
    print("Incluindo ocultos:", db.ler_contatos(1, incluir_ocultos=True))

    # Restaurar contato
    db.restaurar_contato(2)
    print("Contatos após restaurar:", db.ler_contatos(1))

  

    # Fechar conexão
    db.fechar()
    print("\n===== TESTE FINALIZADO =====")

if __name__ == "__main__":
    main()
