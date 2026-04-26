import customtkinter as ctk
from view import settings

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.after(0, lambda: janela.state('zoomed'))
janela.geometry(settings.GEOMETRY)

def janela_init():
    janela.mainloop()