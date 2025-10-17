import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from API.uteis.SELECTORS import css_selectors

def dados_usuario(self):

    #### gerando muito erro, suspenso temporariamente ####
    print("🔄 gerando muito erro, suspenso temporariamente...")
"""

    dados = {}
    try:
        self.buscar_elemento('perfil')
        time.sleep(1)
        # Nome
        elemento_nome = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.xs83m0k.x1g77sc7.xeuugli.x2lwn1j.xozqiw3.x1oa3qoh.x12fk4p8.x1t1x2f9.x1iyjqo2.x37zpob.x6ikm8r.x10wlt62.x14vy60q > div > div'))
        )
        dados['nome'] = elemento_nome.text

        print(f"✅ Dados do usuário obtidos com sucesso: {dados}")


        conversa = self.buscar_elemento('conversa')
        time.sleep(1)  
        conversa.click() 


        return dados
    except Exception as e:
        print("Erro ao obter dados do usuário:", e)
        return None
"""