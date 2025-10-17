import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.bgcolor = ft.Colors.BLACK
    page.theme_mode = ft.ThemeMode.DARK

    

    global usuario
    global senha
    global btn
    usuario = ft.TextField(bgcolor=ft.Colors.PURPLE_800, label="Usuario", width=240, border_radius=15, border_width=4)
    senha = ft.TextField(bgcolor=ft.Colors.PURPLE_800, label="Senha", width=240, border_radius=15, border_width=4)
    
    

    def btn_clicado(e):

        user = "willy"
        password = "1234"

        if usuario.value == user and senha.value == password:
           btn.text="oiii"
           page.update()
    
        
    btn = ft.ElevatedButton("Entrar", on_click=btn_clicado)
    tela_login = ft.Column([usuario, senha, btn], horizontal_alignment="center", width=320, height=270)
    
    conteiner = ft.Stack(
        #width=720,

        controls=[
            ft.Image(src="fundo.jpg", width=1080, height=2340, fit=ft.ImageFit.COVER),
            ft.Container(
                content=ft.Column(
                    controls=[
                        tela_login
                    ],
                    height=150,
                    width=250,
                    alignment=ft.MainAxisAlignment.CENTER
                    
                )
            )
        ],
        height=400,
        alignment=ft.alignment.center
    )
    
    page.add(
        conteiner
    )

ft.app(main)

