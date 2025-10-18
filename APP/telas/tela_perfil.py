import tkinter as tk

from APP.func.verificar_conexao import verificar_conexao


def tela_perfil(self):
    self.limpar_tela()
    self.logado = False  # ⬅ flag de controle global de login

    # Configura o frame principal para crescer
    self.frame_principal.columnconfigure(0, weight=1)
    self.frame_principal.rowconfigure(1, weight=1)  # o conteúdo vai crescer

    # Label de status
    self.label_status = tk.Label(
        self.frame_principal,
        text="Verificando conexão...",
        font=("Arial", 14)
    )
    self.label_status.grid(row=0, column=0, pady=10, sticky="n")  # gruda no topo, mas não trava largura

    # Frame que alterna entre QR e botões
    self.frame_conteudo = tk.Frame(self.frame_principal)
    self.frame_conteudo.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
    self.frame_conteudo.columnconfigure(0, weight=1)
    self.frame_conteudo.rowconfigure(0, weight=1)
    self.frame_conteudo.rowconfigure(1, weight=0)  # botão não precisa expandir verticalmente

    # Label onde o QR será exibido
    self.label_qrcode = tk.Label(self.frame_conteudo, text="Carregando...", font=("Arial", 11))
    self.label_qrcode.grid(row=0, column=0, pady=10, sticky="nsew")

    # Frame dos botões (inicialmente oculto)
    self.frame_botoes = tk.Frame(self.frame_conteudo)
    self.frame_botoes.grid(row=1, column=0, pady=10, sticky="n")  # fixo na parte de baixo
    self.frame_botoes.grid_remove()  # substitui pack_forget

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

    # Inicia a verificação de conexão
    verificar_conexao(self)
