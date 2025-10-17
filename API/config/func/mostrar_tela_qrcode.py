import threading
from PIL import Image, ImageTk


def mostrar_tela_qrcode(self):
    """Exibe o QR Code dentro da tela de perfil."""

    # Se já estiver logado, não faz nada
    if getattr(self, "logado", False):
        return

    def carregar_qrcode():
        try:
            qr_img = self.wd.mostrar_qrcode()
            if qr_img is not None:
                if not isinstance(qr_img, Image.Image):
                    qr_img = Image.fromarray(qr_img)

                qr_img = qr_img.resize((250, 250))
                tk_img = ImageTk.PhotoImage(qr_img)

                def atualizar_label():
                    # Só atualiza se ainda não estiver logado
                    if not getattr(self, "logado", False):
                        self.label_qrcode.configure(image=tk_img, text="")
                        self.label_qrcode.image = tk_img
                        self.label_status.config(text="📱 Escaneie o QR Code para logar.")

                self.frame_principal.after(0, atualizar_label)
            else:
                def mostrar_texto():
                    if not getattr(self, "logado", False):
                        self.label_qrcode.configure(text="Carregando...")
                self.frame_principal.after(0, mostrar_texto)

        except Exception as e:
            print(f"❌ Erro ao carregar QR Code: {e}")

    threading.Thread(target=carregar_qrcode, daemon=True).start()

    # Reagenda atualização apenas se não estiver logado
    if not getattr(self, "logado", False):
        self.frame_principal.after(5000, lambda: mostrar_tela_qrcode(self))