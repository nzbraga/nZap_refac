from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from API.uteis.SELECTORS import css_selectors



def dados_usuario(self):
    self.usuario = []
    """
    Obtém o nome do perfil logado usando o seletor direto que você pegou.
    Retorna o nome como string ou None.
    """
    if not self.driver:
        print("❌ Driver não inicializado.")
        return None
    try:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors.get("perfil")))).click()
        # espera o elemento estar presente
        nome_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selectors.get("nome_business"))  # substitua pelo seletor correto
                )
            )
        numero_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selectors.get("numero_business"))  # substitua pelo seletor correto
                )
            )
        numero_elem.text.strip()
        nome_elem.text.strip()
        self.usuario = [nome_elem.text.strip(), numero_elem.text.strip()]
        
    except Exception as e:
        print(f"⚠️ Não foi possível obter o nome: {e}")
        self.usuario = [None]

    self.driver.refresh()

    return self.usuario