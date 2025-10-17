import tkinter as tk

def criar_menu(self):
    menu_bar = tk.Menu(self.root)

    menu_bar.add_command(label="Perfil", command=self.tela_perfil)
    menu_bar.add_command(label="Mensagem", command=self.tela_mensagem)
    menu_bar.add_command(label="Agendar", command=self.tela_agendamento)

    self.root.config(menu=menu_bar)