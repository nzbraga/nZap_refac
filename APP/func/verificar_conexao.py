import threading
from API.config.func.mostrar_tela_qrcode import mostrar_tela_qrcode


def verificar_conexao(self):
    """Verifica o login periodicamente e alterna QR ↔ botões."""

    def checar():
        try:
            if self.wd.confirmar_login():
                # Marca como logado e para as atualizações
                self.logado = True
                self.label_status.config(text="✅ Conectado com sucesso!")
                self.label_qrcode.pack_forget()
                self.frame_botoes.pack(pady=10)
            else:
                # Continua tentando enquanto não logado
                self.label_status.config(text="Aguardando login no WhatsApp...")
                self.frame_botoes.pack_forget()
                self.label_qrcode.pack(pady=10)
                mostrar_tela_qrcode(self)
                if not getattr(self, "logado", False):
                    self.frame_principal.after(3000, lambda: verificar_conexao(self))
        except Exception as e:
            print(f"⚠️ Erro ao verificar conexão: {e}")
            if not getattr(self, "logado", False):
                self.frame_principal.after(3000, lambda: verificar_conexao(self))

    threading.Thread(target=checar, daemon=True).start()
