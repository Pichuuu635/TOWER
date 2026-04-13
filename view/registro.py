import customtkinter as ctk
from view import settings
from view import janela_ctk
from view.janela_ctk import janela_init

label_register = None

def registro_init():
    
    global frame_registrar
    global entry_registro_nome
    global entry_registro_email
    global entry_registro_password
    global entry_registro_password_confirm
    
    global aviso
    
    
    
    frame_registrar = ctk.CTkFrame(janela_ctk.janela, width=settings.WIDTH, height=settings.HEIGHT, fg_color=settings.COLOR_BACKGROUND)
    frame_registrar.pack()
    
    fonte_1 = ctk.CTkFont(family="Segoe UI", size=60, weight="bold")
    fonte_2 = ctk.CTkFont(family="Segoe UI", size=17)
    
    texto_login = ctk.CTkLabel(frame_registrar, text="Registrar-se", font=fonte_1, text_color=settings.COLOR_TEXT)
    texto_login.place(relx=0.5, rely=0.2, anchor="center")
    
    div_register = ctk.CTkFrame(frame_registrar, width=350, height=150, corner_radius=25, fg_color=settings.COLOR_CARD, bg_color=settings.COLOR_BACKGROUND)
    div_register.place(relx=0.5, rely=0.5, anchor="center")

    fonte_register = ctk.CTkFont(family="Segoe UI", size=18, weight="bold")

    entry_registro_nome = ctk.CTkEntry(div_register, placeholder_text="Nome", width=300, height=45, corner_radius=15, font=fonte_register)
    entry_registro_nome.pack(pady=(15, 15), padx=25)

    entry_registro_email = ctk.CTkEntry(div_register, placeholder_text="Email(Inclua '@'!)", width=300, height=45, corner_radius=15, font=fonte_register)
    entry_registro_email.pack(pady=(0, 15))
    
    entry_registro_password = ctk.CTkEntry(div_register, placeholder_text="Senha", show="*", width=300, height=45, corner_radius=15, font=fonte_register)
    entry_registro_password.pack(pady=(0, 15))
    
    entry_registro_password_confirm = ctk.CTkEntry(div_register, placeholder_text="Confirmar Senha", show="*", width=300, height=45, corner_radius=15, font=fonte_register)
    entry_registro_password_confirm.pack(pady=(0, 15))
    
    botao_registrar = ctk.CTkButton(div_register, width=300, height=40, text="Registrar-se", fg_color=settings.COLOR_PRIMARY, corner_radius=15, font=fonte_register, command=verificar_enviar)
    botao_registrar.pack(pady=(5, 5))
    
    botao_back_login = ctk.CTkButton(div_register, text="Voltar para o Login", fg_color="transparent", hover_color=None, text_color="#3b8ed0", font=ctk.CTkFont(family="Segoe UI", size=13, underline=True), command=back_to_login, width=150)
    botao_back_login.pack(pady=(0, 10))
    
    
    
    def aviso(texto):
        global label_register
        
        if label_register is not None:
            label_register.destroy()
            label_register = None
            
        if texto:
            label_register = ctk.CTkLabel(frame_registrar, text=texto, font=fonte_2, text_color=settings.COLOR_TEXT)
            label_register.place(relx=0.5, rely=0.75, anchor="center")
        
        
    
def verificar_enviar():
    from controller import register_controller
    register_controller.verificar()
    if register_controller.register_funcional == True:
        back_to_login()
        
    
def back_to_login():
    from controller import login_controller
    login_controller.back_login(frame_registrar)