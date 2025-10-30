    # ===== Função de envio =====
def enviar(self):
    destinatario_text = self.destinatario.get()
    mensagem_text = self.mensagem.get("1.0", tk.END).strip()

    # Aqui chamamos a função do WebDriver
    if self.wd is not None:
        sucesso = self.wd.enviar_msg(destinatario_text, mensagem_text)
        if sucesso is False:
            self.notif_label.config(text="❌ Falha ao enviar mensagem!", fg="red")
        else:
            self.notif_label.config(text="✅ Mensagem enviada com sucesso!", fg="green")
            # Limpa o campo de mensagem
            self.mensagem.delete("1.0", tk.END)
    else:
        self.notif_label.config(text="⚠️ WebDriver não iniciado!", fg="orange")
