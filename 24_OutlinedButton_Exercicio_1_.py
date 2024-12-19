"""Crie um aplicativo simples com um OutlinedButton que exibe uma mensagem

Crie uma aplicação básica com um OutlinedButton.
Ao clicar no botão, exiba uma mensagem no console ou em um Text widget na tela."""

import flet as ft
def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 300
    cont = 0

    def exibi(e):
        nonlocal cont
        cont += 1
        print(f'Mensagem {cont} exibida no console!')
        texto_exibido.value= f'Mensagem {cont} exibida do aplicativo!'
        page.update()

    btn = ft.OutlinedButton(
        icon=ft.icons.MESSAGE,
        on_click=exibi
    )

    texto_exibido = ft.Text()
    page.add(btn,texto_exibido)

ft.app(target=main)