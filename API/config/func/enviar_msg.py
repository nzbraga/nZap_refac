

def enviar_msg(self, contato, mensagem):
    print(f"📨 Enviando mensagem para {contato}...")
    try:
        self.buscar_elemento('busca', contato)
        self.buscar_elemento('msg', mensagem)
        print("✅ Mensagem enviada com sucesso!")
    except Exception as e:
        print("Erro ao enviar mensagem:", e)
        return False