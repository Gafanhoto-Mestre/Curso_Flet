"""Exercício 1: Alinhamento de Elementos na Horizontal
Objetivo: Crie uma linha (Row) com três botões. Alinhe esses botões à esquerda, ao centro e à direita dentro da linha.

Dica: Explore as propriedades de alinhamento do Row, como alignment.

Instruções:
Crie três botões (TextButton) com os textos "Esquerda", "Centro", e "Direita".
Coloque esses botões dentro de um Row.
Altere o alinhamento do Row para que os botões fiquem alinhados à esquerda, ao centro, e à direita, respectivamente."""

import flet as ft
def main(page: ft.Page):

    botoes = ft.Row(
        controls=[
        ft.TextButton(text= 'Esquerda'),
        ft.TextButton(text= 'Centro'),
        ft.TextButton(text= 'Direita')],
        alignment= ft.MainAxisAlignment.SPACE_BETWEEN
        )
    
    page.add(botoes)
ft.app(target= main)