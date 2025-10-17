import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from API.uteis.SELECTORS import css_selectors

def buscar_elemento(self, tipo, texto=False):
    print(f"entradas do wb_busca_elemento: {tipo}, {texto}")
    css_selector = css_selectors.get(tipo)
    if not css_selector:
        raise ValueError(f"Tipo '{tipo}' inválido — verifique o dicionário css_selectors")

    elemento = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
    )
    elemento.click()

    if texto:
        elemento.send_keys(Keys.CONTROL + "a")
        time.sleep(0.5)
        elemento.send_keys(Keys.BACKSPACE)
        time.sleep(0.5)
        elemento.send_keys(str(texto) + Keys.ENTER)
        time.sleep(1)
