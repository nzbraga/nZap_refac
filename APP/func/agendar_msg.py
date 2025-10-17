def agendar(destinatario, mensagem, frequencia, data):
    if not destinatario:
        print("Erro: Destinatário não pode estar vazio.")
    elif not mensagem:
        print("Erro: Mensagem não pode estar vazia.")
    elif frequencia not in ["Uma vez", "Diária", "Semanal", "Mensal", "Anual"]:
        print("Erro: Frequência inválida.")
    elif data == "":
        print("Erro: Data inválida.")
    else:
        print("Mensagem agendada com sucesso!")
    
    print("Agendando mensagem...")
    print("Destinatário:",destinatario)
    print("Mensagem:", mensagem)
    print("Frequência:", frequencia)
    print("Data escolhida:", data)
