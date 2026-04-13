import customtkinter as ctk
from view import settings
from view import janela_ctk
from view.janela_ctk import janela_init


def dashboard_init():
    
    frame_dashboard = ctk.CTkFrame(janela_ctk.janela, fg_color=settings.COLOR_BACKGROUND, width=settings.WIDTH, height=settings.HEIGHT)
    frame_dashboard.pack()
    
    
    
    
    
    janela_init()