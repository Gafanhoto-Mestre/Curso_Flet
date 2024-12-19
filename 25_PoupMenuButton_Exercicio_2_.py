"""Exercício 2: Menu de seleção de tema
Crie um PopupMenuButton com várias opções de temas (por exemplo, "Tema Claro", "Tema Escuro", "Tema Azul").
Ao selecionar um tema, altere o fundo da página e as cores dos textos conforme o tema escolhido."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()

    def cor(e):
        if e.control.text == "Tema Amber":
            page.bgcolor = ft.colors.AMBER
        elif e.control.text == "Tema Azul":
            page.bgcolor = ft.colors.BLUE
        elif e.control.text == "Tema Vermelho":
            page.bgcolor = ft.colors.RED

        page.update()
    
    cores = [
        ft.PopupMenuItem(text= 'Tema Amber', on_click= cor),
        ft.PopupMenuItem(text= "Tema Azul", on_click= cor),
        ft.PopupMenuItem(text= "Tema Vermelho", on_click= cor)
    ]

    pb = ft.PopupMenuButton(items=cores)

    page.add(pb)
ft.app(target= main)