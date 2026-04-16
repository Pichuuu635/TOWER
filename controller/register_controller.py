import customtkinter as ctk
import json
import os
from view.registro import registro_init
from view import registro

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_JSON = os.path.join(BASE_DIR, "..", "data", "usuarios.json")
def registrar(frame_destruir):
    frame_destruir.destroy()
    registro_init()
    
def verificar():
    global password_funcional
    global texto_label_register
    global register_funcional
    register_funcional = False
    texto_label_register = None
    
    nome_data = registro.entry_registro_nome.get().strip()
    email_data = registro.entry_registro_email.get().strip()
    password_data = registro.entry_registro_password.get()
    password_confirm_data = registro.entry_registro_password_confirm.get()
    
    if not nome_data or len(nome_data) <= 3:
        nome_data_funcional = False
        texto_label_register = "Precisa Incluir Nome com mínimo \n 3 caracteres"
    else:
        nome_data_funcional = True
        
    if not password_data or len(password_data) <= 4:
        password_data_funcional = False
        texto_label_register = "Precisa Incluir Senha com \n mínimo 5 caracteres"
    else:
        password_data_funcional = True
        
        
        
    if "@" in email_data:
       email_funcional = True
       
       if password_data == password_confirm_data:
        global password_funcional
        password_funcional = True
    
       else:
           password_funcional = False
           texto_label_register = "As senhas não conferem"
       
    else:
        email_funcional = False
        texto_label_register = "O email é invalido, deve incluir '@'"
        
    if texto_label_register is not None:
        
        registro.aviso(texto_label_register)
        
    print(email_funcional, password_data_funcional, nome_data_funcional, password_data_funcional)
    
    if email_funcional == True and password_funcional == True and nome_data_funcional == True and password_data_funcional == True:
        texto_label_register = "Registro Concluido!"
        register_funcional = True

    if register_funcional == True:
        registrar_usuario(nome_data, email_data, password_data)
        print("I got here!")

        print(nome_data, email_data, password_data, password_confirm_data)    

def carregar_usuarios():
    if not os.path.exists(CAMINHO_JSON):
        return []
    try:
        with open(CAMINHO_JSON, "r") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def registrar_usuario(nome, email, senha):
    usuarios = carregar_usuarios()
    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "planta": ""
    }
    usuarios.append(novo_usuario)
    salvar_usuario(usuarios)

def salvar_usuario(user):
    os.makedirs(os.path.dirname(CAMINHO_JSON), exist_ok=True)
    with open(CAMINHO_JSON, "w") as arquivo:
        json.dump(user, arquivo, indent=4)

    
    
    
    
    
    
    
     
