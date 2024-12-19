"""Exercício 4: Menu Responsivo
Objetivo: Crie um menu de navegação responsivo usando ResponsiveRow, onde os itens de menu aparecem em uma linha em telas grandes e empilhados verticalmente em telas pequenas.

Dica: Utilize a propriedade col para ajustar o layout em diferentes tamanhos de tela.

Instruções:
Crie quatro botões de menu (TextButton) com textos como "Home", "Sobre", "Serviços", e "Contato".
Adicione os botões ao ResponsiveRow, configurando-os para ocupar 3 colunas em telas grandes e 12 colunas em telas pequenas."""

import flet as ft
def main(page: ft.Page):
    
    menu = ft.ResponsiveRow(
        controls=[
            ft.TextButton(text= "Home", col={"sm": 3, "sm": 3}),
            ft.TextButton(text= "Sobre", col={"sm": 3, "sm": 3}),
            ft.TextButton(text= "Serviços", col={"sm": 3, "sm": 3}),
            ft.TextButton(text= "Contato", col={"sm": 3, "sm": 3})
        ]
    )

    page.add(menu)
ft.app(target= main)