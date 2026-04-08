import customtkinter as ctk
import settings
from controller import login_controller
import janela_ctk
from janela_ctk import janela_init


def login_exibir():

    janela_init
    
    frame_login = ctk.CTkFrame(janela_ctk.janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BACKGROUND)
    frame_login.pack()

    div_login = ctk.CTkFrame(frame_login, width=350, height=150, corner_radius=25, fg_color=settings.COLOR_CARD, bg_color=settings.COLOR_BACKGROUND)
    div_login.place(relx=0.5, rely=0.5, anchor="center")

    fonte_login = ctk.CTkFont(family="Segoe UI", size=18, weight="bold")

    entry_login = ctk.CTkEntry(div_login, placeholder_text="Login/Email", width=300, height=45, corner_radius=15, font=fonte_login)
    entry_login.pack(pady=(15, 10), padx=20)

    entry_password_login = ctk.CTkEntry(div_login, placeholder_text="Password", show="*", width=300, height=45, corner_radius=15, font=fonte_login)
    entry_password_login.pack(pady=(0, 10))
    botao_login = ctk.CTkButton(div_login, width=300, height=40, text="Entrar", fg_color=settings.COLOR_PRIMARY, corner_radius=15, font=fonte_login, command=lambda:login_controller.verificar(entry_login.get(), entry_password_login.get()))
    botao_login.pack(pady=(5, 15))



    #janela_ctk.janela.mainloop()

login_exibir()
