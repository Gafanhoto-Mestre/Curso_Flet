"""Mude a cor do botão ao clicar

Crie um OutlinedButton que altere sua cor ao ser clicado.
Use diferentes cores para cada estado (clicado ou não clicado)."""

import flet as ft
from random import randint
from time import sleep

cores = {
    1: ft.colors.AMBER,
    2: ft.colors.RED_500,
    3: ft.colors.BLUE,
    4: ft.colors.GREEN
}

def main(page: ft.Page):
    page.window.width = 400
    page.window.height =300

    def alterando(e):
        contador = 0
        while contador < 10:
            cor = randint(1,4)
            estilo = ft.ButtonStyle(
                bgcolor= cores[cor]
            )
            btn.style = estilo
            cor_exibida.value = f'Cor número {cor}!'
            sleep(1)
            contador += 1
            contando.value = f'Contagem {contador}...'
            if contador == 10:
                fim.value = 'Fim da contagem, até logo!'
            page.update()

    btn = ft.OutlinedButton(
        text='Alterar cor',
        icon= ft.icons.COLOR_LENS,
        on_click=alterando,
    )
    
    cor_exibida = ft.Text()
    contando = ft.Text()
    fim = ft.Text()
    page.add(btn, cor_exibida, contando, fim)

ft.app(target=main, view= ft.WEB_BROWSER)