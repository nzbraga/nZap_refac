import tkinter as tk


def tela_mensagem(self):
    self.limpar_tela()

    # ===== Título =====
    titulo = tk.Label(
        self.frame_principal,
        text="Enviar Mensagem",
        font=("Arial", 18, "bold"),
        pady=10
    )
    titulo.pack()

    # ===== Container principal =====
    container = tk.Frame(self.frame_principal, padx=20, pady=20)
    container.pack(fill="both", expand=True)

    # ===== Campo: Destinatário =====
    tk.Label(container, text="Enviar para:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
    destinatario = tk.Entry(container, width=40, font=("Arial", 11))
    destinatario.grid(row=0, column=1, pady=5, padx=10)

    # ===== Campo: Mensagem =====
    tk.Label(container, text="Mensagem:", font=("Arial", 12)).grid(row=1, column=0, sticky="nw", pady=5)
    mensagem = tk.Text(container, width=40, height=6, font=("Arial", 11))
    mensagem.grid(row=1, column=1, pady=5, padx=10)

    # ===== Label de notificação =====
    notif_label = tk.Label(self.frame_principal, text="", font=("Arial", 12, "bold"))
    notif_label.pack(pady=5)

    # ===== Função de envio =====
    def enviar():
        destinatario_text = destinatario.get()
        mensagem_text = mensagem.get("1.0", tk.END).strip()

        # Aqui chamamos a função do WebDriver
        if self.wd is not None:
            sucesso = self.wd.enviar_msg(destinatario_text, mensagem_text)
            if sucesso is False:
                notif_label.config(text="❌ Falha ao enviar mensagem!", fg="red")
            else:
                notif_label.config(text="✅ Mensagem enviada com sucesso!", fg="green")
                # Limpa o campo de mensagem
                mensagem.delete("1.0", tk.END)
        else:
            notif_label.config(text="⚠️ WebDriver não iniciado!", fg="orange")

    # ===== Botão Enviar =====
    btn_enviar = tk.Button(
        self.frame_principal,
        text="📨 Enviar Mensagem",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=enviar
    )
    btn_enviar.pack(pady=20)

    # ===== Foco automático =====
    destinatario.focus_set()
