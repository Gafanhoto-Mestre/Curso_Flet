"""Exercício 1: Container com Borda e Sombra
Crie um Container com um texto centralizado. Adicione uma borda ao redor do container e aplique uma sombra para dar a impressão de elevação. Personalize a cor da borda e a cor da sombra.

Dicas:

Utilize as propriedades border, border_radius e box_shadow.
Centralize o texto usando a propriedade alignment."""

import flet as ft
def main(page: ft.Page):
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.bgcolor= ft.colors.AMBER

    container= ft.Container(
        content= ft.Text(value= 'Texto centralizado', color= ft.colors.BLACK, size= 20),
        bgcolor= ft.colors.BLUE,
        width= 500,
        height= 500,
        alignment= ft.alignment.center,
        border= ft.border.all(10, color= ft.colors.ORANGE),
        border_radius= ft.border_radius.all(20),
        shadow= ft.BoxShadow(
            blur_radius= 30,
            color= ft.colors.RED,
            offset= ft.Offset(x=30, y=-30)

        )
    )
    


    page.add(container)
ft.app(target= main)