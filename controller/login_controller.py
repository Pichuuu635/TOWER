import customtkinter as ctk
import json
from view.dashboard import dashboard_init
from view import settings
from view.registro import registro_init
from view.login import login_exibir
from controller.register_controller import carregar_usuarios

email_em_banco_de_dados = "admin"
senha_em_banco_de_dados = "tower123"

def verificar(email, senha, frame_destruir):
    gave_email = email.lower()
    gave_senha = senha
    
    print(email)
    print(senha)
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["email"] == gave_email and usuario["senha"] == gave_senha:
            frame_destruir.destroy()
            dashboard_init()
    
    
def back_login(frame_destruir):
    frame_destruir.destroy()
    login_exibir()

