from API.config.func.mostrar_tela_qrcode import mostrar_tela_qrcode
import threading

def verificar_conexao(self):
    """Verifica o login periodicamente e alterna QR ↔ botões."""

    def checar():
        try:
            # Se já estiver logado, apenas atualiza a interface e não repete
            if getattr(self, "logado", False):
                self.label_status.config(text="✅ Conectado com sucesso!")
                self.label_qrcode.grid_remove()
                self.frame_botoes.grid()  # mostra botões
                return

            # Verifica o status de login
            if self.wd.confirmar_login():
                self.logado = True
                self.label_status.config(text="✅ Conectado com sucesso!")
                self.label_qrcode.grid_remove()
                self.frame_botoes.grid()  # mostra botões
            else:
                # Ainda não logado → mostra QR
                self.logado = False
                self.label_status.config(text="Aguardando login no WhatsApp...")
                self.frame_botoes.grid_remove()
                self.label_qrcode.grid()
                mostrar_tela_qrcode(self)

                # Agenda nova verificação
                self.frame_principal.after(3000, lambda: verificar_conexao(self))

        except Exception as e:
            print(f"⚠️ Erro ao verificar conexão: {e}")
            if not getattr(self, "logado", False):
                self.frame_principal.after(3000, lambda: verificar_conexao(self))

    threading.Thread(target=checar, daemon=True).start()

