import os

def definir_diretorio(self):
        self.PROFILE_DIR = os.path.expanduser(f"~/.whatsapp_API_{self.client}")
        return self.PROFILE_DIR
