from view.dashboard import dashboard_init
from view import settings

email_em_banco_de_dados = "admin"
senha_em_banco_de_dados = "tower123"

def verificar(email, senha, frame_destruir):
    teste_email = email.lower()
    teste_senha = senha
    
    print(email)
    print(senha)
    if teste_email == "admin":
        if teste_senha == "tower123":
            print("Cheguei ate aq")
            #from view.login import frame_login
            frame_destruir.destroy()
            dashboard_init()
            print("Cheguei ate aq")
            