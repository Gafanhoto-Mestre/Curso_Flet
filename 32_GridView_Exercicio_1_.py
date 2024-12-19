"""Exercício 1: GridView Básico com Imagens
Crie uma galeria de imagens usando o GridView. Adicione pelo menos 6 imagens, organizando-as em 2 colunas. As imagens devem se ajustar ao tamanho da célula do GridView.

Dicas:

Utilize a propriedade grid_fit para ajustar as imagens ao tamanho das células.
Defina o número de colunas usando a propriedade crossAxisCount."""

import flet as ft
def main(page: ft.Page):

    grid = ft.GridView(
        controls= [
            ft.Image(src= f'https://picsum.photos/250/300?{num}',fit= 'cover') for num in range(6)
        ],
        runs_count= 2,
        child_aspect_ratio= 0.56

    )

    page.add(grid)
ft.app(target= main)