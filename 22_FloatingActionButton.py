# FloatingActionButton

import flet as ft
def main(page: ft.Page):
    page.window.width = 300    # Define a LARGURA   
    page.window.height = 400    # Define a ALTURA
    page.floating_action_button = ft.FloatingActionButton(   
        icon= ft.icons.ADD,
        #bgcolor= ft.colors.LIGHT_BLUE_100, # Define a cor do botão
        mini=True,  #  Se "True" deixa o botão menor
        shape= ft.CircleBorder(),  # O botão fica redondo
        tooltip= "Mensagem ao passar o mouse",
        # text='Tem como colocar um texto'
        on_click= lambda _: print("Clicou!")
    )
    page.update()
ft.app(target=main, view=ft.WEB_BROWSER)