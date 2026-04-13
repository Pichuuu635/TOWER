import customtkinter as ctk
from view import settings
from view import janela_ctk
from view.janela_ctk import janela_init


def dashboard_init():
    
    frame_dashboard = ctk.CTkFrame(janela_ctk.janela, fg_color=settings.COLOR_BACKGROUND, width=settings.WIDTH, height=settings.HEIGHT)
    frame_dashboard.pack()

    fonte_1 = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")

    label_dashboard = ctk.CTkLabel(frame_dashboard, text="Dashboard", font=fonte_1, fg_color=settings.COLOR_TEXT)
    
    
    
    
    
    janela_init()