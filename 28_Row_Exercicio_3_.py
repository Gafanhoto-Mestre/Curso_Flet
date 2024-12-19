"""Exercício 3: Criação de uma Linha Responsiva
Objetivo: Crie uma linha (Row) que contenha diferentes elementos (por exemplo, uma imagem, um texto, e um botão). A linha deve se ajustar ao tamanho da janela, mantendo os elementos visíveis e adequadamente dimensionados.

Dica: Use a propriedade expand e configure a responsividade dos controles para se ajustar ao tamanho da janela.

Instruções:
Adicione uma imagem (Image), um texto (Text), e um botão (IconButton) dentro de um Row.
Configure o Row para que os elementos se ajustem ao tamanho da janela.
Teste redimensionando a janela para ver como os elementos se comportam."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 800
    page.window.height= 300
    page.window.center()
    
    linha = ft.Row(
        controls=[
            ft.Image(src= "images/logo.png", width=100, height=100, expand= 1),
            ft.Text(value= "Texto responsivo", expand= 2),
            ft.IconButton(icon= ft.icons.ADD, expand= 1)
        ],
        
    )

    page.add(linha)
ft.app(target= main)