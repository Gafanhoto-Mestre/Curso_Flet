"""Exercício 3: Layout Responsivo para Imagens
Objetivo: Crie um layout que exiba quatro imagens lado a lado em telas grandes e em duas colunas em telas médias. Em telas pequenas, as imagens devem ser dispostas uma abaixo da outra.

Dica: Configure diferentes valores de col para cada tamanho de tela.

Instruções:
Adicione quatro imagens (Image) ao ResponsiveRow.
Configure o col de cada imagem para 3 colunas em telas grandes, 6 colunas em telas médias, e 12 colunas em telas pequenas."""

import flet as ft
def main(page: ft.Page):
    page.scroll= True

    img = ft.ResponsiveRow(   
        spacing= 20,  
        controls=[
            ft.Image(src= "images/redenova.png", col={"md": 6, "lg": 3}),
            ft.Image(src= "images/redenova.png", col={"md": 6, "lg": 3}),
            ft.Image(src= "images/redenova.png", col={"md": 6, "lg": 3}),
            ft.Image(src= "images/redenova.png", col={"md": 6, "lg": 3})
        ]
    )

    page.add(img)
ft.app(target= main)