import customtkinter as ctk
import settings
import janela_ctk


def dashboard_init():
    dashboard_janela = ctk.CTk()
    dashboard_janela.after(0, lambda: janela_ctk.janela.state('zoomed'))
    dashboard_janela.geometry(settings.GEOMETRY)
    
    
    
    
    
    dashboard_janela.mainloop()