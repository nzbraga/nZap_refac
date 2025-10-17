import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from API.uteis.SELECTORS import css_selectors

def enviar_doc(self, contato, caminho_arquivo):

    
    print(f"Enviando documento para {contato}: {caminho_arquivo}")
"""
    try:
        if not os.path.exists(caminho_arquivo):
            print("❌ Arquivo não encontrado.")
            return False

        # Buscar o contato
        self.buscar_elemento('busca', contato)

        # Clicar no ícone de clipe
        anexo_btn = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selectors.get("anexar"))))
        anexo_btn.click()

        upload = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selectors.get("upload"))))
        upload.send_keys(caminho_arquivo)

        enviar_btn = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, css_selectors.get("enviar_btn"))))
        enviar_btn.click()

        print("✅ Documento enviado com sucesso!")
        return True

    except Exception as e:
        print("Erro ao enviar documento:", e)
        return False
"""