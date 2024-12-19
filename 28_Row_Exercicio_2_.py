"""Exercício 2: Distribuição Uniforme de Espaço
Objetivo: Crie uma linha (Row) com quatro caixas de texto (TextField), distribuídas uniformemente ao longo da linha.

Dica: Use a propriedade expand nos controles e a propriedade spacing no Row para gerenciar o espaço entre os elementos.

Instruções:
Crie quatro caixas de texto (TextField) com diferentes label.
Coloque essas caixas dentro de um Row.
Configure o Row para que as caixas de texto ocupem o espaço disponível uniformemente."""

import flet as ft
def main(page: ft.Page):
    
    linha = ft.Row(
        controls=[
            ft.TextField(label= "Campo 1", expand= True),
            ft.TextField(label= "Campo 2", expand= True),
            ft.TextField(label= "Campo 3", expand= True),
            ft.TextField(label= "Campo 4", expand= True)
        ],
        spacing= 10
    )

    page.add(linha)
ft.app(target= main)