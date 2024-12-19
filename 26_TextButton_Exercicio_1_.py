"""1. Alternar Visibilidade de um Componente
Objetivo: Crie um layout com um TextButton que, ao ser clicado, alterna a visibilidade de um PopupMenuButton. O menu deve ter duas opções: "Mostrar" e "Ocultar".
Dica: Use uma variável booleana para rastrear a visibilidade do menu e altere seu estado no evento on_click do TextButton."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()
    
    # Variável para rastrear a visibilidade do PopupMenuButton
    visivel = True

    # Função para alternar a visibilidade do PopupMenuButton
    def alternar(e):
        nonlocal visivel
        visivel = not visivel # Alterna entre False e True (o termo not significa o contrário)
        pb.visible = visivel
        page.update()
        
    tx = ft.TextButton(text= "Alternar Menu", style= ft.ButtonStyle(color= ft.colors.LIGHT_BLUE_600), on_click= alternar, data= False)

    opc = [ft.PopupMenuItem(text= "Mostrar"),
             ft.PopupMenuItem(text= "Ocultar")
             ]

    pb = ft.PopupMenuButton(items= opc)

    page.add(tx, pb)
ft.app(target= main)