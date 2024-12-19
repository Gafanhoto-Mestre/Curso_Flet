# 18_Icones

import flet as ft

def main(page: ft.Page):
    page.window.width = 400 # Definir o largura da janela
    page.window.height = 500 # Definir a altura da janela

    icon1 = ft.Icon(name=ft.icons.KEY, color=ft.colors.LIGHT_GREEN_500) # Adiciona o ícone, também alterei a cor

    icone2 = ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK_400, size=60, tooltip='Favoritos') # Adicionei o ícone, alterei a cor e adiconei o tooltip quendo o usuário passa o moude por cima da imagem

    icon3 = ft.Icon(name=ft.icons.LOGIN) # Adicionei o íconé pesquisando em 'https://flet.dev/docs/controls/icon/'

    icon4 = ft.Image(src='zap24.png')

    page.add(icon1, icone2, icon3,icon4)


ft.app(target=main)
