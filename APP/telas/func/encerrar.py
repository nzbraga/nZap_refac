import sys
def encerrar(self):
    print("\n🧹 Encerrando aplicação...")

    # Fecha o WebDriver se estiver ativo
    if self.wd is not None:
        try:
            self.wd.fechar()
        except Exception as e:
            print(f"⚠️ Erro ao encerrar WebDriver: {e}")

    # Destroi a janela e encerra o programa
    self.root.destroy()
    sys.exit(0)
