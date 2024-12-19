"""Alteração de ícone e cor ao clicar

Crie um IconButton que altere seu ícone e cor ao ser clicado.
Use diferentes ícones e cores para cada estado (clicado ou não clicado)."""

import flet as ft
def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 400

    page.window.width = 300
    page.window.height = 400

    def alterar(e):
        e.control.selected = not e.control.selected
        e.control.update()
        

    btn = ft.IconButton(
        icon= ft.icons.PLAY_CIRCLE_FILLED_ROUNDED,
        icon_size= 50,
        selected_icon= ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
        selected=False,
        on_click= alterar,
        style= ft.ButtonStyle(
            color={
                ft.MaterialState.SELECTED: ft.colors.AMBER_400,
            }
        )
    )

    page.add(btn)

    page.add(btn)

ft.app(target=main)