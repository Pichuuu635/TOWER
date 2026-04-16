import customtkinter as ctk
from view import settings
from view import janela_ctk
from view.janela_ctk import janela_init
from data import tower_data
from data import estufa_data



def dashboard_init():

    temp_data = f"{estufa_data.temperatura_ar}°C"
    umid_data = f"{estufa_data.umidade_ar}% (Ar)"
    umid_soil_data = f"{estufa_data.umidade_solo}% (Solo)"
    
    frame_dashboard = ctk.CTkFrame(janela_ctk.janela, fg_color=settings.COLOR_BACKGROUND, width=settings.WIDTH, height=settings.HEIGHT)
    frame_dashboard.pack()

    fonte_1 = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")
    fonte_2 = ctk.CTkFont(family="Segoe UI", size=35, weight="bold")
    fonte_3 = ctk.CTkFont(family="Segoe UI", size=50, weight="bold")
    fonte_4 = ctk.CTkFont(family="Segoe UI", size=30, weight="bold")

    label_dashboard = ctk.CTkLabel(frame_dashboard, text="Estufa - Dashboard", font=fonte_1, text_color=settings.COLOR_ACCENT)
    label_dashboard.place(relx=0.5, rely=0.07, anchor="center")

    div_dashboard = ctk.CTkFrame(frame_dashboard, width=1250, height=600, corner_radius=35, fg_color=settings.COLOR_CARD, bg_color=settings.COLOR_BACKGROUND)
    div_dashboard.place(relx=0.5, rely=0.55, anchor="center")

    div_data_dashboard = ctk.CTkFrame(div_dashboard, width=366, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35)
    div_data_dashboard.place(x=33, y=12.5, anchor="nw")
    
    label_info_data_dashboard = ctk.CTkLabel(div_data_dashboard, text="Informações:", font=fonte_2, text_color=settings.COLOR_EXTRA)
    label_info_data_dashboard.place(x=20, y=5)
    
    label_temp_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=temp_data, font=fonte_4, text_color=settings.COLOR_EXTRA)
    label_temp_data_dashboard.place(x=25, y=55)
    
    label_umid_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=umid_data, font=fonte_4, text_color=settings.COLOR_EXTRA)
    label_umid_data_dashboard.place(x=25, y=105)
    
    label_umid_soil_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=umid_soil_data, font=fonte_4, text_color=settings.COLOR_EXTRA)
    label_umid_soil_data_dashboard.place(x=25, y=155)
    
    div_tower1_dashboard = ctk.CTkFrame(div_dashboard, width=251, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35)
    div_tower1_dashboard.place(x=432, y=12.5)
    
    label_tower1 = ctk.CTkLabel(div_tower1_dashboard, text="Torre 1:", font=fonte_2, text_color=settings.COLOR_EXTRA)
    label_tower1.place(x=20, y=5)

    div_tower2_dashboard = ctk.CTkFrame(div_dashboard, width=251, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35)
    div_tower2_dashboard.place(x=699, y=12.5)

    label_tower2 = ctk.CTkLabel(div_tower2_dashboard, text="Torre 2:", font=fonte_2, text_color=settings.COLOR_EXTRA)
    label_tower2.place(x=20, y=5)
    
    div_tower3_dashboard = ctk.CTkFrame(div_dashboard, width=251, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35)
    div_tower3_dashboard.place(x=966, y=12.5)
    
    label_tower3 = ctk.CTkLabel(div_tower3_dashboard, text="Torre 3:", font=fonte_2, text_color=settings.COLOR_EXTRA)
    label_tower3.place(x=20, y=5)
    
    div_status_dashboard = ctk.CTkFrame(div_dashboard, width=400, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35)
    div_status_dashboard.place(x=33, y=300)
    
    label_status_dashboard = ctk.CTkLabel(div_status_dashboard, text="Status:", font=fonte_2, text_color=settings.COLOR_EXTRA)
    label_status_dashboard.place(x=20, y=5)
    
    div_alerta_dashboard = ctk.CTkFrame(div_dashboard, width=757, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35)
    div_alerta_dashboard.place(x=463, y=300)
    
    label_status_dashboard = ctk.CTkLabel(div_alerta_dashboard, text="Alertas:", font=fonte_3, text_color=settings.COLOR_EXTRA)
    label_status_dashboard.place(x=378.5, y=30, anchor="center")
    
    frame_linha_status_dashboard = ctk.CTkFrame(div_alerta_dashboard, width=737, height=4, fg_color=settings.COLOR_EXTRA2)
    frame_linha_status_dashboard.place(x=10, y=70)



    
    
    janela_init()
    
