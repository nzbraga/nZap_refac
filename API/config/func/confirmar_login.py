from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from API.uteis.SELECTORS import css_selectors

def confirmar_login(self):
    self.css_selector = css_selectors.get('perfil')
    try:
        logado = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_selector))
        )
        print("✅ Login confirmado")
        return True

    except: 
        return False
