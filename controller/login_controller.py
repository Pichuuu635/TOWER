from view.dashboard import dashboard_init
from view import settings
from view.registro import registro_init
from view.login import login_exibir

email_em_banco_de_dados = "admin"
senha_em_banco_de_dados = "tower123"

def verificar(email, senha, frame_destruir):
    teste_email = email.lower()
    teste_senha = senha
    
    print(email)
    print(senha)
    if teste_email == "admin":
        if teste_senha == "tower123":
            frame_destruir.destroy()
            dashboard_init()
        else:
            print("Senha Incorreta")
    else:
            print("Usuário Incorreto")

    frame_destruir.destroy()
    registro_init()
    
def back_login(frame_destruir):
    frame_destruir.destroy()
    login_exibir()

