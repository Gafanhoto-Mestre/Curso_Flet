"""Exibir uma imagem ao clicar no botão

Crie um OutlinedButton que, ao ser clicado, exibe uma imagem na tela.
A imagem pode ser carregada de um URL ou de um arquivo local."""

import flet as ft
def main(page: ft.Page):
    page.title= "Meu aplicativo"
    page.window.width = 300
    page.window.height = 300
    page.window.center()

    def imagem(e):
        img = ft.Image(src='images/slogan.png')
        page.add(img)
        #btn.url = 'https://learnersgalaxy.ai/wp-content/uploads/2024/01/Python-Symbol.png'
        page.scroll = True
        page.update()
  
    btn = ft.OutlinedButton(
        text= 'Mostrar imagem',
        icon= ft.icons.IMAGE,
        on_click=imagem
    )

    page.add(btn)
ft.app(target=main, assets_dir='assets' ) #, view= ft.WEB_BROWSER)