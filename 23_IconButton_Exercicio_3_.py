"""Contador de cliques

Crie um IconButton que conta quantas vezes foi clicado.
Exiba o contador em um Text widget."""

import flet as ft
def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 400
    cont = 0

    def soma(e):
        nonlocal cont
        cont += 1
        somatoria.value = cont
        page.update()

    btn = ft.IconButton(
        icon= ft.icons.ADD,
        on_click= soma,
    )

    somatoria = ft.Text()

    page.add(btn, somatoria)
ft.app(target=main)