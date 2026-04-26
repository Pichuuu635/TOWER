import customtkinter as ctk
import threading
from view import settings
from view import janela_ctk
from view.janela_ctk import janela_init
from data import tower_data
from data import data_reader_estufa
from data import data_reader_tower
from controller import data_receive



def dashboard_init():

    
    
    dados_estufa = data_reader_estufa.ler_ultimo_estufa()
    dados_tower = data_reader_tower.ler_ultimo_estufa()

    if dados_estufa:
        temp_data = f"{dados_estufa['temperatura']}°C"
        umid_data = f"{dados_estufa['umidade']}% (Ar)"
        umid_soil_data = f"{dados_estufa['solo_d0']}% (Solo)"
        rain_estufa = {dados_tower['chuva']}
        if rain_estufa == 1:
            rain_estufa = "Chovendo"
        else:
            rain_estufa = "Sem chuva"

    if dados_tower:
        temp_tower = f"{dados_tower['temperatura']}°C"
        umid_tower = f"{dados_tower['umidade']}% (Ar)"
        rain_tower = {dados_tower['chuva']}
        if rain_tower == 1:
            rain_tower = "Chovendo"
        else:
            rain_tower = "Sem chuva"


    
    frame_dashboard = ctk.CTkFrame(janela_ctk.janela, fg_color=settings.COLOR_BACKGROUND, width=settings.WIDTH, height=settings.HEIGHT)
    frame_dashboard.pack()

    fonte_1 = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")
    fonte_2 = ctk.CTkFont(family="Segoe UI", size=35, weight="bold")
    fonte_3 = ctk.CTkFont(family="Segoe UI", size=50, weight="bold")
    fonte_4 = ctk.CTkFont(family="Segoe UI", size=30, weight="bold")

    label_dashboard = ctk.CTkLabel(frame_dashboard, text="Estufa - Dashboard", font=fonte_1, text_color=settings.COLOR_HIGHLIGHT)
    label_dashboard.place(relx=0.5, rely=0.07, anchor="center")

    div_dashboard = ctk.CTkFrame(frame_dashboard, width=1250, height=600, corner_radius=35, fg_color=settings.COLOR_CARD, bg_color=settings.COLOR_BACKGROUND, border_color=settings.COLOR_BORDER, border_width=2)
    div_dashboard.place(relx=0.5, rely=0.55, anchor="center")

    div_data_dashboard = ctk.CTkFrame(div_dashboard, width=366, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35, border_color=settings.COLOR_SECONDARY, border_width=2)
    div_data_dashboard.place(x=33, y=12.5, anchor="nw")
    
    label_info_data_dashboard = ctk.CTkLabel(div_data_dashboard, text="Informações:", font=fonte_2, text_color=settings.COLOR_ACCENT)
    label_info_data_dashboard.place(x=20, y=5)
    
    label_temp_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=temp_data, font=fonte_4, text_color=settings.COLOR_PRIMARY)
    label_temp_data_dashboard.place(x=25, y=55)
    
    label_umid_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=umid_data, font=fonte_4, text_color=settings.COLOR_PRIMARY)
    label_umid_data_dashboard.place(x=25, y=105)
    
    label_umid_soil_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=umid_soil_data, font=fonte_4, text_color=settings.COLOR_PRIMARY)
    label_umid_soil_data_dashboard.place(x=25, y=155)

    label_rain_data_dashboard = ctk.CTkLabel(div_data_dashboard, text=rain_estufa, font=fonte_4, text_color=settings.COLOR_PRIMARY)
    label_rain_data_dashboard.place(x=25, y=205)
    
    div_tower1_dashboard = ctk.CTkFrame(div_dashboard, width=251, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35, border_color=settings.COLOR_BORDER, border_width=2)
    div_tower1_dashboard.place(x=432, y=12.5)

    label_temp_tower_dashboard = ctk.CTkLabel(div_tower1_dashboard, text=temp_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_temp_tower_dashboard.place(x=25, y=55)
    
    label_umid_tower_dashboard = ctk.CTkLabel(div_tower1_dashboard, text=umid_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_umid_tower_dashboard.place(x=25, y=105)
    
    label_rain_tower_dashboard = ctk.CTkLabel(div_tower1_dashboard, text=rain_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_rain_tower_dashboard.place(x=25, y=155)
    
    label_tower1 = ctk.CTkLabel(div_tower1_dashboard, text="Torre 1:", font=fonte_2, text_color=settings.COLOR_HIGHLIGHT)
    label_tower1.place(x=20, y=5)

    div_tower2_dashboard = ctk.CTkFrame(div_dashboard, width=251, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35, border_color=settings.COLOR_BORDER, border_width=2)
    div_tower2_dashboard.place(x=699, y=12.5)

    label_tower2 = ctk.CTkLabel(div_tower2_dashboard, text="Torre 2:", font=fonte_2, text_color=settings.COLOR_HIGHLIGHT)
    label_tower2.place(x=20, y=5)

    label_temp_tower2_dashboard = ctk.CTkLabel(div_tower2_dashboard, text=temp_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_temp_tower2_dashboard.place(x=25, y=55)
    
    label_umid_tower2_dashboard = ctk.CTkLabel(div_tower2_dashboard, text=umid_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_umid_tower2_dashboard.place(x=25, y=105)
    
    label_rain_tower2_dashboard = ctk.CTkLabel(div_tower2_dashboard, text=rain_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_rain_tower2_dashboard.place(x=25, y=155)
    
    div_tower3_dashboard = ctk.CTkFrame(div_dashboard, width=251, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35, border_color=settings.COLOR_BORDER, border_width=2)
    div_tower3_dashboard.place(x=966, y=12.5)
    
    label_tower3 = ctk.CTkLabel(div_tower3_dashboard, text="Torre 3:", font=fonte_2, text_color=settings.COLOR_HIGHLIGHT)
    label_tower3.place(x=20, y=5)

    label_temp_tower3_dashboard = ctk.CTkLabel(div_tower3_dashboard, text=temp_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_temp_tower3_dashboard.place(x=25, y=55)
    
    label_umid_tower3_dashboard = ctk.CTkLabel(div_tower3_dashboard, text=umid_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_umid_tower3_dashboard.place(x=25, y=105)
    
    label_rain_tower3_dashboard = ctk.CTkLabel(div_tower3_dashboard, text=rain_tower, font=fonte_4, text_color=settings.COLOR_ACCENT)
    label_rain_tower3_dashboard.place(x=25, y=155)

    div_status_dashboard = ctk.CTkFrame(div_dashboard, width=400, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35, border_color=settings.COLOR_BORDER, border_width=2)
    div_status_dashboard.place(x=33, y=300)
    
    label_status_dashboard = ctk.CTkLabel(div_status_dashboard, text="Status:", font=fonte_2, text_color=settings.COLOR_HIGHLIGHT)
    label_status_dashboard.place(x=20, y=5)
    
    div_alerta_dashboard = ctk.CTkFrame(div_dashboard, width=757, height=275, fg_color=settings.COLOR_CARD_2, corner_radius=35, border_color=settings.COLOR_BORDER, border_width=2)
    div_alerta_dashboard.place(x=463, y=300)
    
    label_status_dashboard = ctk.CTkLabel(div_alerta_dashboard, text="Alertas:", font=fonte_3, text_color=settings.COLOR_HIGHLIGHT)
    label_status_dashboard.place(x=378.5, y=30, anchor="center")
    
    frame_linha_status_dashboard = ctk.CTkFrame(div_alerta_dashboard, width=737, height=4, fg_color=settings.COLOR_SECONDARY)
    frame_linha_status_dashboard.place(x=10, y=70)



    
    threading.Thread(target=data_receive.iniciar_servidor, daemon=True).start()
    janela_init()
    
