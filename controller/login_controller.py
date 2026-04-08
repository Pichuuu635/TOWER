from view.dashboard import dashboard_init
from view import login
from view import settings

email_em_banco_de_dados = "admin"
senha_em_banco_de_dados = "tower123"

def verificar(email, senha):
    print(email)
    print(senha)
    if email.lower() == email_em_banco_de_dados:
        if senha == senha_em_banco_de_dados:
            login.frame_login.destroy()
            dashboard_init()
            