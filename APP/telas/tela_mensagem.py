import tkinter as tk
from APP.func.enviar_msg import enviar


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
    self.container = tk.Frame(self.frame_principal, padx=20, pady=20)
    self.container.pack(fill="both", expand=True)

    # ===== Campo: Destinatário =====
    tk.Label(self.container, text="Lista de envio:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)

    self.btn_abrir_lista = tk.Button(
        self.container,
        text="📨 Abrir Lista",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=print("abir lista")
    )
    self.btn_abrir_lista.grid(row=0, column=1, pady=10)


    # ===== Campo: Mensagem =====
    tk.Label(self.container, text="Mensagem:", font=("Arial", 12)).grid(row=1, column=0, sticky="nw", pady=5)
    self.mensagem = tk.Text(self.container, width=40, height=6, font=("Arial", 11))
    self.mensagem.grid(row=1, column=1, pady=5, padx=10)

    # Frame horizontal para alinhar combobox e DateEntry
    self.notif_label = tk.Frame(self.container)
    self.notif_label.grid(row=2, column=1, pady=5, padx=10, sticky="we")

    # ===== Botão Enviar =====
    btn_enviar = tk.Button(
        self.container,
        text="📨 Enviar Mensagem",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=enviar(self)
    )
    btn_enviar.grid(row=3, column=1, pady=10)

    # ===== Foco automático =====
    self.destinatario.focus_set()





