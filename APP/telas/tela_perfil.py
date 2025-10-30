import tkinter as tk
from APP.telas.func.verificar_conexao import verificar_conexao


def tela_perfil(self):
    self.limpar_tela()

    # Garante que a flag exista
    if not hasattr(self, "logado"):
        self.logado = False

    # Frame principal ocupa toda a janela
    self.frame_principal.columnconfigure(0, weight=1)
    self.frame_principal.rowconfigure(0, weight=1)

    # Frame central
    self.frame_central = tk.Frame(self.frame_principal)
    self.frame_central.grid(row=0, column=0, sticky="nsew")
    self.frame_central.columnconfigure(0, weight=1)
    self.frame_central.rowconfigure(0, weight=1)

    # Subframe centralizado
    self.frame_conteudo = tk.Frame(self.frame_central)
    self.frame_conteudo.pack(expand=True)
    self.frame_conteudo.columnconfigure(0, weight=1)

    # Label de status
    self.label_status = tk.Label(
        self.frame_conteudo,
        text="Verificando conexão..." if not self.logado else "✅ Conectado com sucesso!",
        font=("Arial", 14),
        anchor="center",
        justify="center"
    )
    self.label_status.grid(row=0, column=0, pady=10, sticky="n")

    # Label QR Code
    self.label_qrcode = tk.Label(
        self.frame_conteudo,
        text="Carregando...",
        font=("Arial", 11),
        anchor="center",
        justify="center"
    )
    self.label_qrcode.grid(row=1, column=0, pady=20, sticky="n")

    # Frame dos botões
    self.frame_botoes = tk.Frame(self.frame_conteudo)
    self.frame_botoes.grid(row=2, column=0, pady=10)

    tk.Label(self.frame_botoes, text="Perfil", font=("Arial", 14)).pack(pady=20)

    tk.Button(
        self.frame_botoes,
        text="Desconectar nZap",
        command=lambda: self.wd.fechar(),
        bg="light blue",
        fg="black",
        width=20,
        height=2
    ).pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    tk.Button(
        self.frame_botoes,
        text="Desconectar WhatsApp",
        bg="light green",
        fg="black",
        command=lambda: self.wd.fechar(),
        width=20,
        height=2
    ).pack(side=tk.LEFT, padx=5, expand=True, fill="x")

    # Se estiver logado, mostra direto os botões
    if self.logado:
        self.label_qrcode.grid_remove()
        self.frame_botoes.grid()
    else:
        self.frame_botoes.grid_remove()
        verificar_conexao(self)
