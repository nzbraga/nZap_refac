from API.config.func.iniciar import iniciar
from API.config.func.fechar import fechar
from API.config.func.dados_usuario import dados_usuario
from API.config.func.definir_diretorio import definir_diretorio
from API.config.func.confirmar_login import confirmar_login 
from API.config.func.mostrar_qrcode import mostrar_qrcode
from API.config.func.mostrar_tela_qrcode import mostrar_tela_qrcode
from API.config.func.buscar_elemento import buscar_elemento
from API.config.func.enviar_msg import enviar_msg
from API.config.func.enviar_doc import enviar_doc
from API.config.func.dados_usuario import dados_usuario


class WebDriver:
    def __init__(self, client, headless=False):
        self.client = client
        self.headless = headless
        self.driver = None
        self.diretorio = self.definir_diretorio()

    iniciar = iniciar
    fechar = fechar
    dados_usuario = dados_usuario
    definir_diretorio = definir_diretorio
    confirmar_login = confirmar_login
    mostrar_qrcode = mostrar_qrcode
    mostrar_tela_qrcode = mostrar_tela_qrcode
    buscar_elemento = buscar_elemento
    enviar_msg = enviar_msg 
    enviar_doc = enviar_doc
    dados_usuario = dados_usuario
  