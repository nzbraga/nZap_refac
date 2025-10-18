import tkinter as tk
import threading

from API.config.WebDriver import WebDriver

from APP.func.criar_menu import criar_menu
from APP.func.limpar_tela import limpar_tela

from APP.telas.tela_perfil import tela_perfil
from APP.telas.tela_mensagem import tela_mensagem
from APP.telas.tela_agendamento import tela_agendamento
from APP.telas.tela_config import tela_config



class AppInterface:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("nZap")
        self.root.geometry("500x400")

        #self.root.resizable(False, False)
        #self.root.attributes('-toolwindow', True) 

        self.wd = WebDriver(client="test_default", headless=False)
        threading.Thread(target=self.wd.iniciar, daemon=True).start()
        # Cria o menu de navegação
        self.criar_menu()

        # Cria o frame principal
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(fill="both", expand=True)

        # Exibe a tela inicial
        self.tela_perfil()

        self.root.mainloop()
        
       
    #MENUS E NAVEGAÇÃO
    criar_menu = criar_menu

    #FUNÇÕES 
    limpar_tela = limpar_tela
    

    #TELAS
    tela_perfil = tela_perfil
    tela_mensagem = tela_mensagem
    tela_agendamento = tela_agendamento
    tela_config = tela_config





