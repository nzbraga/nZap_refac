import psutil

def fechar(self):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] in ('chrome', 'chrome.exe'):
                cmdline = " ".join(proc.info['cmdline'])
                if '--user-data-dir=' in cmdline and str(self.diretorio) in cmdline:
                    proc.terminate()
                    proc.wait(timeout=5)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"✅ Navegador fechado para o cliente '{self.client}'.")
