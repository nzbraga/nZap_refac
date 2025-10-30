import io
import base64
import time
import threading

from PIL import Image, ImageTk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from API.uteis.SELECTORS import css_selectors


def mostrar_tela_qrcode(self):
    """Mostra e atualiza o QR Code na tela de perfil, parando quando logado."""

    # Cancela temporizadores antigos (evita múltiplas chamadas simultâneas)
    if hasattr(self, "_timer_qr") and self._timer_qr is not None:
        self.frame_principal.after_cancel(self._timer_qr)
        self._timer_qr = None

    # Se já estiver logado, não faz nada
    if getattr(self, "logado", False):
        return

    def carregar_qrcode():
        """Executa em thread separada para não travar a interface."""
        try:
            # Tenta obter o QR Code do navegador (até 5 tentativas)
            tentativa = 0
            qr_img = None

            while tentativa < 5 and not getattr(self, "logado", False):
                tentativa += 1
                try:
                    print(f"🔍 Tentando localizar QR Code (tentativa {tentativa}/5)...")

                    qr_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors.get("qrcode")))
                    )

                    qr_base64 = self.driver.execute_script(
                        "return arguments[0].toDataURL('image/png').substring(22);", qr_element
                    )
                    qr_bytes = base64.b64decode(qr_base64)
                    qr_img = Image.open(io.BytesIO(qr_bytes))
                    break  # encontrou, sai do loop

                except Exception as e:
                    print(f"❌ QR Code não encontrado (tentativa {tentativa}/5): {e}")
                    if tentativa < 5 and not getattr(self, "logado", False):
                        print("⏳ Tentando novamente em 3 segundos...\n")
                        time.sleep(3)

            # Se encontrou a imagem, atualiza a interface
            if qr_img is not None and not getattr(self, "logado", False):
                qr_img = qr_img.resize((250, 250))
                tk_img = ImageTk.PhotoImage(qr_img)

                def atualizar_label():
                    if not getattr(self, "logado", False):
                        self.label_qrcode.configure(image=tk_img, text="")
                        self.label_qrcode.image = tk_img
                        self.label_status.config(text="📱 Escaneie o QR Code para logar.")
                self.frame_principal.after(0, atualizar_label)

            else:
                # QR Code não disponível
                def mostrar_texto():
                    if not getattr(self, "logado", False):
                        self.label_qrcode.configure(image="", text="Aguardando QR Code...")
                        self.label_status.config(text="🔄 Tentando carregar QR Code...")
                self.frame_principal.after(0, mostrar_texto)

        except Exception as e:
            print(f"❌ Erro ao carregar QR Code: {e}")

    # Executa o carregamento em thread separada
    threading.Thread(target=carregar_qrcode, daemon=True).start()

    # Reagenda atualização a cada 5 segundos (somente se não logado)
    if not getattr(self, "logado", False):
        self._timer_qr = self.frame_principal.after(5000, lambda: mostrar_tela_qrcode(self))
