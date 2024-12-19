"""Desabilitar/Ativar funcionalidade

Crie dois IconButton: um para desativar e outro para ativar um terceiro IconButton.
Quando o botão de desativar for clicado, desative o terceiro IconButton.
Quando o botão de ativar for clicado, ative o terceiro IconButton."""

import flet as ft
def main(page: ft.Page):
    def ativar(e):
        btn3.disabled = False
        btn3.tooltip = 'Botão ativado!'
        page.update()

    def desativar(e):
        btn3.disabled = True
        btn3.tooltip = 'Botão desativado!'
        page.update()

    bnt1 = ft.IconButton(icon=ft.icons.LOOKS_ONE, on_click=ativar)

    btn2 = ft.IconButton(icon= ft.icons.LOOKS_TWO, on_click=desativar)

    btn3 = ft.IconButton(icon= ft.icons.LOOKS_3, tooltip='Botão ativado!')

    page.add(bnt1, btn2, btn3)
ft.app(target=main)