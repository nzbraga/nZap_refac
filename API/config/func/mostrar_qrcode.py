import io
import base64
import qrcode_terminal

from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from API.uteis.SELECTORS import css_selectors

def mostrar_qrcode(self):
    self.tentativa = 0
    while self.tentativa < 5:
        self.tentativa += 1
        try:
            qr_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors.get("qrcode")))
            )
            qr_base64 = self.driver.execute_script(
                "return arguments[0].toDataURL('image/png').substring(22);", qr_element
            )
            qr_bytes = base64.b64decode(qr_base64)
            img = Image.open(io.BytesIO(qr_bytes))
            print("\n📱 Escaneie o QR Code abaixo com seu WhatsApp:\n")
            qrcode_terminal.draw(img)
            return img
        except Exception as e:
            print(f"❌ QR Code não encontrado. Tentativa {self.tentativa}/5")
            if self.tentativa < 3:
                print("⏳ Tentando novamente...")
    return None