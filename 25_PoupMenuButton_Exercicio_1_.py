"""Exercício 1: Menu de opções de usuário
Crie um PopupMenuButton com opções como "Perfil", "Configurações" e "Sair".
Ao selecionar uma opção, exiba uma mensagem correspondente à opção selecionada."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()

    def captura(e):
        elemento = e.control.text
        msg.value = f'Você selecionou: {elemento}'
        msg.italic = True
        page.update()
        
    pb = ft.PopupMenuButton(
        icon= ft.icons.LIST,
        tooltip= 'Inicio',
        items= [
            ft.PopupMenuItem(text= "Perfil", icon= ft.icons.ASSIGNMENT_IND, on_click= captura),
            ft.PopupMenuItem(text= "Configurações", icon= ft.icons.SETTINGS, on_click= captura),
            ft.PopupMenuItem(text= "Sair", icon= ft.icons.EXIT_TO_APP, on_click= captura)
        ]
    )

    msg = ft.Text()

    page.add(pb,msg)
ft.app(target=main)