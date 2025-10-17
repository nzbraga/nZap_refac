import tkinter as tk


def tela_config(self):
    self.limpar_tela()

    # ===== Título =====
    titulo = tk.Label(
        self.frame_principal,
        text="Configurações",
        font=("Arial", 18, "bold"),
        pady=10
    )
    titulo.pack()

    # ===== Container principal =====
    container = tk.Frame(self.frame_principal, padx=20, pady=20)
    container.pack(fill="both", expand=True)

    # ===== Campo: Remetente =====
    tk.Label(container, text="Remetente:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
    remetente = tk.Entry(container, width=25, font=("Arial", 11))
    remetente.grid(row=0, column=1, pady=5, padx=10, columnspan=2, sticky="we")

    # ===== Campo: Horário de envio =====
    tk.Label(container, text="Horário de envio:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)

    # Subcontainer para alinhar as horas nos extremos
    frame_horas = tk.Frame(container)
    frame_horas.grid(row=1, column=1, columnspan=2, sticky="we", padx=10)

    frame_horas.columnconfigure(0, weight=1)
    frame_horas.columnconfigure(1, weight=1)

    hora_inicio = tk.Entry(frame_horas, width=10, font=("Arial", 11))
    hora_inicio.grid(row=0, column=0, sticky="w")

    hora_final = tk.Entry(frame_horas, width=10, font=("Arial", 11))
    hora_final.grid(row=0, column=1, sticky="e")

    # ===== Campo: Intervalo de envio =====
    tk.Label(container, text="Intervalo de envio (min):", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
    intervalo_envio = tk.Entry(container, width=25, font=("Arial", 11))
    intervalo_envio.grid(row=2, column=1, pady=5, padx=10, columnspan=2, sticky="we")

    # ===== Função de envio =====
    def salvar_config():
        print("Salvando configurações...")
        print(f"Remetente: {remetente.get()}")
        print(f"Hora início: {hora_inicio.get()}")
        print(f"Hora final: {hora_final.get()}")
        print(f"Intervalo: {intervalo_envio.get()}")

    # ===== Botão Salvar =====
    btn_salvar = tk.Button(
        container,
        text="💾 Salvar Configurações",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        command=salvar_config
    )
    btn_salvar.grid(row=3, column=1, columnspan=2, pady=15)

    # ===== Foco automático =====
    remetente.focus_set()
