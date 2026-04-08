import customtkinter as ctk
import settings
import janela_ctk
from janela_ctk import janela_init


def dashboard_init():
    
    frame_dashboard = ctk.CTkFrame(janela_ctk.janela, fg_color="#36ff14", width=settings.WIDTH, height=settings.HEIGHT)
    frame_dashboard.pack()
    
    
    
    
    
    janela_init()