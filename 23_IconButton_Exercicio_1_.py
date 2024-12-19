"""Aula 23 - Crie um aplicativo simples com um IconButton que exibe uma mensagem

Crie uma aplicação básica com um IconButton.
Ao clicar no botão, exiba uma mensagem no console ou em um Text widget na tela."""

import flet as ft
def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 400

    def clique(e):
        e.control.botao = print('Clicou!')

    botao = ft.IconButton(
        icon= ft.icons.ADS_CLICK,
        on_click=clique
    )

    page.add(botao)
ft.app(target=main)