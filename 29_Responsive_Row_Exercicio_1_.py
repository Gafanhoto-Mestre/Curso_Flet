"""Exercício 1: Layout Responsivo com Diferentes Colunas
Objetivo: Crie uma interface que organize quatro caixas de texto (TextField) em uma linha utilizando o ResponsiveRow. As caixas devem se reorganizar em duas colunas quando a largura da tela for reduzida.

Dica: Use a propriedade col em cada item do ResponsiveRow para definir como eles devem se comportar em diferentes larguras de tela.

Instruções:
Crie quatro caixas de texto (TextField).
Adicione cada uma em um ResponsiveRow com col configurado para ocupar 3 colunas em telas grandes (12 colunas total) e 6 colunas em telas menores (duas por linha)."""

import flet as ft
def main(page: ft.Page):
    
    linha = ft.ResponsiveRow(
        expand=True,
        controls=[
            ft.TextField(value= "Campo 1",col={"xs": 12,"md": 6,"lg": 3}),
            ft.TextField(value= "Campo 2",col={"xs": 12,"md": 6,"lg": 3}),
            ft.TextField(value= "Campo 3",col={"xs": 12,"md": 6,"lg": 3}),
            ft.TextField(value= "Campo 4",col={"xs": 12,"md": 6,"lg": 3})
        ]
    )

    page.add(linha)
ft.app(target= main)