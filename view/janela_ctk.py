import customtkinter as ctk
from view import settings



janela = ctk.CTk()
janela.after(0, lambda: janela.state('zoomed'))
janela.geometry(settings.GEOMETRY)

def janela_init():
    janela.mainloop()