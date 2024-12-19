"""Habilitar/Desabilitar outro botão

Crie dois OutlinedButton: um para desativar e outro para ativar um terceiro OutlinedButton.
Quando o botão de desativar for clicado, desative o terceiro OutlinedButton.
Quando o botão de ativar for clicado, ative o terceiro OutlinedButton."""

import flet as ft
def main(page: ft.Page):
    page.title= 'Exercício 5'
    page.window.width = 300
    page.window.height = 300
    page.window.center()

    def home(e):
        btn3.text = 'Lets Go! '
        btn3.icon= ft.icons.SENTIMENT_NEUTRAL_ROUNDED
        btn3.icon_color= ft.colors.YELLOW
        btn3.style= ft.ButtonStyle(padding= ft.alignment.center)        
        page.update()

    def Ativar(e):
        btn3.disabled= False
        btn3.text= 'Ativado'
        btn3.icon = ft.icons.SENTIMENT_VERY_SATISFIED
        btn3.icon_color= ft.colors.GREEN
        btn3.tooltip = ""
        page.update()

    def Desativar(e):
        btn3.text= 'Desativado'
        btn3.disabled= True
        btn3.icon= ft.icons.SENTIMENT_DISSATISFIED_ROUNDED
        btn3.icon_color= ft.colors.GREY_300
        btn3.tooltip= 'Opção desativada!'
        page.update()

    btn = ft.OutlinedButton(
                            text= 'Página inicial',
                            icon= ft.icons.HOME, 
                            on_click= home, 
                            width= 200)

    btn1 = ft.OutlinedButton(text= 'Ativar', icon= ft.icons.CHECK,
                            icon_color= ft.colors.GREEN,
                            on_click=Ativar,
                            width= 200)

    btn2 = ft.OutlinedButton(text= 'Desativar', icon= ft.icons.BLOCK,
                            icon_color= ft.colors.RED,
                            on_click=Desativar,
                            width= 200)

    btn3 = ft.OutlinedButton(
        width= 200,
        text= 'Lets Go!',
        icon= ft.icons.SENTIMENT_NEUTRAL_ROUNDED,
        icon_color= ft.colors.YELLOW,
        style= ft.ButtonStyle(
            padding= ft.alignment.center
        )        
    )

    page.add(btn, btn1, btn2, btn3)
    page.update()
ft.app(target=main)