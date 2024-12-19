import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()

    btn = ft.TextButton(
        'Enviar',
        icon= ft.icons.SEND,
        icon_color= ft.colors.LIGHT_BLUE,
        tooltip= 'Olá uma mensagem',
        url= 'www.google.com.br',
        style= ft.ButtonStyle( color= ft.colors.RED),
        on_click= lambda _: print("Olá Mundo!")
    )

    page.add(btn)
ft.app(target= main)