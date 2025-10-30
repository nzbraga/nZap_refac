import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


def iniciar(self):
    """Inicia o driver do WhatsApp Web, fechando instâncias antigas do próprio app."""

    # 🔹 Fecha driver antigo se ainda estiver ativo
    try:
        if hasattr(self, "driver") and self.driver:
            self.driver.quit()
            print("🧹 Navegador anterior fechado com sucesso.")
            time.sleep(1)
    except Exception as e:
        print(f"⚠️ Erro ao fechar navegador anterior: {e}")

    # 🔹 Configurações do Chrome
    self.options = webdriver.ChromeOptions()
    self.options.page_load_strategy = 'eager'
    self.options.add_argument("--disable-gpu")
    self.options.add_argument("--no-sandbox")
    self.options.add_argument("--no-first-run")
    self.options.add_argument("--disable-infobars")
    self.options.add_argument("--disable-dev-shm-usage")
    self.options.add_argument(f"user-data-dir={self.definir_diretorio()}")

    if getattr(self, "headless", False):
        self.options.add_argument("--headless=new")

    # 🔹 Inicia o navegador
    try:
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://web.whatsapp.com")
        print("✅ Navegador iniciado e WhatsApp Web carregando...")
    except Exception as e:
        print(f"❌ Erro ao iniciar navegador: {e}")
        self.driver = None


