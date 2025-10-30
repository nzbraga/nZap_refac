def limpar_tela(self):
    for widget in self.frame_principal.winfo_children():
        widget.destroy()