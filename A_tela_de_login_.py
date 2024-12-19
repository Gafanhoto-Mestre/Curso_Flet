import flet as ft

def main(page: ft.Page):
    # Centraliza o conteúdo na página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title= "DataSAM"
    page.theme_mode= "dark"

    linha = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(src="images/logo1.png", width=300),
                ft.TextField(
                    label="Usuário", 
                    width=300,
                    border_radius=20
                ),
                ft.TextField(
                    label="Senha", 
                    password=True, 
                    width=300,
                    border_radius=20
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Entrar", width=150, icon= ft.icons.LOGIN),
                        ft.ElevatedButton(text="Cadastrar", width=150, icon= ft.icons.PERSON_ADD)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10  # Adiciona um espaçamento entre os botões
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente os controles dentro da coluna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza horizontalmente os controles
        ),
        alignment=ft.alignment.center
    )
    
    # Adiciona o container à página
    page.add(linha)

ft.app(target=main, view= ft.WEB_BROWSER)