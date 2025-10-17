import tkinter as tk

from APP.func.verificar_conexao import verificar_conexao


def tela_perfil(self):
    self.limpar_tela()
    self.logado = False  # ⬅ flag de controle global de login


    # Label de status
    self.label_status = tk.Label(
        self.frame_principal,
        text="Verificando conexão...",
        font=("Arial", 14)
    )
    self.label_status.pack(pady=10)

    # Frame que alterna entre QR e botões
    self.frame_conteudo = tk.Frame(self.frame_principal)
    self.frame_conteudo.pack(pady=10)

    # Label onde o QR será exibido
    self.label_qrcode = tk.Label(self.frame_conteudo, text="Carregando...", font=("Arial", 11))
    self.label_qrcode.pack(pady=10)

    # Frame dos botões (inicialmente oculto)
    self.frame_botoes = tk.Frame(self.frame_conteudo)
    self.frame_botoes.pack_forget()

    tk.Label(self.frame_botoes, text="Perfil", font=("Arial", 14)).pack(pady=20)

    tk.Button(
        self.frame_botoes,
        text="Desconectar nZap",
        command=lambda: self.wd.fechar(),
        bg="light blue",
        fg="black",
        width=20,
        height=2
    ).pack(side=tk.LEFT, padx=5)

    tk.Button(
        self.frame_botoes,
        text="Desconectar WhatsApp",
        bg="light green",
        fg="black",
        command=lambda: self.wd.fechar(),
        width=20,
        height=2
    ).pack(side=tk.LEFT, padx=5)

    # Inicia a verificação de conexão
    verificar_conexao(self)
