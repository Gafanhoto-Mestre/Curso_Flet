"""2. Menu de Seleção de Cor
Objetivo: Crie um PopupMenuButton com opções de cores ("Vermelho", "Verde", "Azul") e um TextButton que, ao ser clicado, exibe o nome da cor selecionada em um Text.
Dica: Utilize o evento on_click dos PopupMenuItem para armazenar a cor selecionada e exibi-la ao clicar no TextButton."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 300
    page.window.height= 300
    page.window.center()

    cor_selecionada = ft.Text(value= "Nenhuma cor selecionada!")

    def cor(e):
        cor_selecionada.value = e.control.text
        page.update()

    menu = ft.PopupMenuButton(
    items=[
      ft.PopupMenuItem(text = 'Vermelho', on_click= cor),
      ft.PopupMenuItem(text= 'Verde', on_click= cor),
      ft.PopupMenuItem(text= 'Azul', on_click= cor)
    ]
  )

    botao_cor = ft.TextButton(text= 'Cor selecionada', on_click= lambda _: print(cor_selecionada.value))

    page.add(menu, botao_cor, cor_selecionada)
ft.app(main)