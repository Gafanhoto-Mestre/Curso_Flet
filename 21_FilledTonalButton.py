# 21_ FilledTonalButton.

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height=600
    botao1= ft.FilledTonalButton(text='Botão secundário')

    page.add(
        ft.FilledTonalButton(text='Botão secundário'),
        ft.FilledTonalButton(text='Botão secundário desabilitado', disabled=True),
        ft.FilledTonalButton(text='Botão secundário com ícone', icon= ft.icons.ADD),
        ft.FilledTonalButton(text='Botão secundário com ícone colorido', icon=ft.icons.ADD, icon_color=ft.colors.PINK),
        ft.FilledTonalButton(text='Botão secundário com tootip', tooltip='Olá'),
        ft.FilledTonalButton(text='Botão com estilo', style= ft.ButtonStyle(bgcolor=ft.colors.AMBER, color={ft.MaterialState.HOVERED: ft.colors.BLUE, ft.MaterialState.DEFAULT: ft.colors.PINK}, animation_duration=1000, shape=ft.RoundedRectangleBorder(radius=5))))

    page.add(botao1)
    page.update()
ft.app(target=main)