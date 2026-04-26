import customtkinter as ctk
from view import settings
from view import janela_ctk
from view.janela_ctk import janela_init


    
def login_exibir():

    global frame_login
    global entry_password_login
    global entry_login
    
    frame_login = ctk.CTkFrame(janela_ctk.janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BACKGROUND)
    frame_login.pack()

    fonte_1 = ctk.CTkFont(family="Segoe UI", size=65, weight="bold")
    
    texto_login = ctk.CTkLabel(frame_login, text="T.O.W.E.R.", font=fonte_1, text_color=settings.COLOR_ACCENT)
    texto_login.place(relx=0.5, rely=0.2, anchor="center")
     
    div_login = ctk.CTkFrame(frame_login, width=350, height=150, corner_radius=25, fg_color=settings.COLOR_CARD, bg_color=settings.COLOR_BACKGROUND, border_color=settings.COLOR_BORDER, border_width=2)
    div_login.place(relx=0.5, rely=0.5, anchor="center")


    fonte_login = ctk.CTkFont(family="Segoe UI", size=18, weight="bold")

    entry_login = ctk.CTkEntry(div_login, placeholder_text="Login/Email", width=300, height=45, corner_radius=15, font=fonte_login)
    entry_login.pack(pady=(15, 10), padx=20)

    entry_password_login = ctk.CTkEntry(div_login, placeholder_text="Password", show="*", width=300, height=45, corner_radius=15, font=fonte_login)
    entry_password_login.pack(pady=(0, 10))

    botao_login = ctk.CTkButton(div_login, width=300, height=40, text="Entrar", fg_color=settings.COLOR_PRIMARY, hover_color=settings.COLOR_SECONDARY, corner_radius=15, font=fonte_login, command=clique)
    botao_login.pack(pady=(5, 5))

    botao_registrar = ctk.CTkButton(div_login, text="Não tem conta? Registre-se", fg_color="transparent", hover_color=settings.COLOR_CARD_2, text_color=settings.COLOR_LINK, font=ctk.CTkFont(family="Segoe UI", size=13, underline=True), command=registrar, width=190)
    botao_registrar.pack(pady=(0, 10))

    
        
    janela_init()
    
def clique():
    from controller import login_controller    
    login_controller.verificar(entry_login.get(), entry_password_login.get(), frame_login)   

def registrar():
    from controller import register_controller
    register_controller.registrar(frame_login)

    
login_exibir()
