import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from APP.telas.func.agendar_msg import agendar

def tela_agendamento(self):
    self.limpar_tela()

    # ===== Título =====
    titulo = tk.Label(
        self.frame_principal,
        text="Agendar Mensagem",
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

    # ===== Campo: Frequência + Data =====
    tk.Label(container, text="Frequência:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)

    # Frame horizontal para alinhar combobox e DateEntry
    freq_data_frame = tk.Frame(container)
    freq_data_frame.grid(row=2, column=1, pady=5, padx=10, sticky="we")

    # Combobox à esquerda
    frequencia_var = tk.StringVar()
    frequencia_combo = ttk.Combobox(
        freq_data_frame,
        textvariable=frequencia_var,
        values=["Uma vez", "Diária", "Semanal", "Mensal", "Anual"],
        state="readonly",
        font=("Arial", 11),
        width=12
    )
    frequencia_combo.pack(side="left", anchor="w")
    frequencia_combo.current(0)

    # DateEntry à direita
    data_entry = DateEntry(
        freq_data_frame,
        width=12,
        font=("Arial", 11),
        background='darkblue',
        foreground='white',
        borderwidth=2,
        date_pattern='dd/mm/yyyy'
    )
    data_entry.pack(side="right", anchor="e")

    btn_abrir_modelos = tk.Button(
        container,
        text="📋 Modelos",
        bg="#2196F3",
        fg="white",
        font=("Arial", 10, "bold"),
        width=10,
        height=1,
        command=print("abrir modelos")
    )
    btn_abrir_modelos.grid(row=2, column=1,pady=5)

    btn_salvar_modelo = tk.Button(
        container,
        text="💾 Salvar Modelo",
        bg="#FF9800",
        fg="white",
        font=("Arial", 10, "bold"),
        width=15,
        height=1,
        command=print("salvar modelo")
    )
    btn_salvar_modelo.grid(row=2, column=2,pady=5)
    # ===== Label de notificação =====
    notif_label = tk.Label(self.frame_principal, text="", font=("Arial", 12, "bold"))
    notif_label.pack(pady=5)



    # ===== Botão Enviar =====
    btn_enviar = tk.Button(
        container,
        text="📨 Agendar Mensagem",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=agendar(
            destinatario.get(),
            mensagem.get("1.0", "end").strip(),
            frequencia_var.get(),
            data_entry.get())
    )
    btn_enviar.grid(row=4, column=1, pady=10)

    # ===== Foco automático =====
    destinatario.focus_set()
