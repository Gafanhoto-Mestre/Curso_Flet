"""Exercício 3: Menu de idiomas
Crie um PopupMenuButton com opções de idiomas (por exemplo, "Inglês", "Espanhol", "Português").
Ao selecionar um idioma, altere o texto na página para o idioma correspondente."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 300
    page.window.height = 300
    page.window.center()

    def idioma(e):
        lingua = e.control.text
        if lingua == "Inglês":
            exibir.value = 'Hello World!'
            exibir.color = ft.colors.RED
        elif lingua == "Espanhol":
            exibir.value = "Hola Mundo!"
            exibir.color = ft.colors.AMBER
        elif lingua == "Italiano":
            exibir.value = "Ciao Mondo!"
            exibir.color = ft.colors.BLUE
        page.update()

    opcoes = [
        ft.PopupMenuItem(text= "Inglês", on_click= idioma),
        ft.PopupMenuItem(text= "Espanhol", on_click= idioma),
        ft.PopupMenuItem(text= "Italiano", on_click= idioma)
    ]
    
    menu = ft.PopupMenuButton(items=opcoes, icon= ft.icons.LIST)
    exibir = ft.Text(value= "Escolha um idioma")
    page.add(menu, exibir)
ft.app(main)