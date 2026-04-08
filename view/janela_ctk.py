import customtkinter as ctk
import settings


def janela_init():
    janela = ctk.CTk()
    janela.after(0, lambda: janela.state('zoomed'))
    janela.geometry(settings.GEOMETRY)

    janela.mainloop()