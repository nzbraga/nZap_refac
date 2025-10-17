from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC


def iniciar(self):
    self.options = webdriver.ChromeOptions()
    self.options.page_load_strategy = 'eager'
    self.options.add_argument("--disable-gpu")
    self.options.add_argument("--no-sandbox")
    self.options.add_argument("--no-first-run")
    self.options.add_argument("--disable-infobars")
    self.options.add_argument("--disable-dev-shm-usage")
    self.options.add_argument(f"user-data-dir={self.definir_diretorio()}")

    if self.headless:
        self.options.add_argument("--headless=new")

    self.driver = webdriver.Chrome(options=self.options)
    self.driver.get("https://web.whatsapp.com")
