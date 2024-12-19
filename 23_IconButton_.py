# IconButton (ft.)    Ícone como Botão

import flet as ft
def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 400

    bt1 =  ft.IconButton(       
        icon= ft.icons.DELETE_FOREVER_ROUNDED,  # Ícone de PLAY
        icon_color= ft.colors.AMBER, # Define a cor do ícone
        icon_size= 50, # Define o tamanho do ícone (em pixels)
        tooltip='Mensagem tooltip' # Define a mensagem tooltip
    )

    def play_pause(e):
        e.control.selected = not e.control.selected
        e.control.update()

    btn2 = ft.IconButton(
        icon= ft.icons.PLAY_CIRCLE, # Ícone padrão
        icon_size=100, # Tamanho do ícone
        selected_icon= ft.icons.PAUSE_CIRCLE, # Ícone que muda ao ser clicaco!
        selected=True,
        on_click= play_pause, # Comando para o botão
        style= ft.ButtonStyle(   #  Definindo o estilo do ícone padrão
            color={
                ft.MaterialState.DEFAULT: ft.colors.GREY_500, # Estilo do ícone padrão
                ft.MaterialState.SELECTED: ft.colors.LIGHT_BLUE_400 # Estilo do ícone ao ser clicado! 
                }
        )
    )
    bt = ft.IconButton(
        icon= ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
        icon_size=30,
        icon_color= ft.colors.GREEN,
        tooltip='Iniciar'
    )
    page.add(bt1, btn2, bt)
    page.update()

ft.app(target=main)