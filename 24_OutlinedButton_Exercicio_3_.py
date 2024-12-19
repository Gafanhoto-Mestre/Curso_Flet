"""Botão contador

Crie um OutlinedButton que conta quantas vezes foi clicado.
Exiba o contador em um Text widget."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 300

    numeral = 0
    regresso = 10
    
    def contador(e):
        # e.control.data += 1
        # if e.control.data > 10:
        #     num.value = f'num: {e.control.data}'
        #     num2.value = f'num2: {(e.control.data) - 3}'

        # num2.value = f'num2: {e.control.data}'
        # btn.update()
        
        # ou

        nonlocal numeral
        nonlocal regresso
        numeral += 1
        if numeral > 10:
            num.value= f'num: {numeral}'
            if numeral < 20:
                regresso -= 1
                num2.value = f'num2: {regresso}'
            else:
                num2.value= 'Acabou a regressão!'
            btn.update
        else:
            num2.value= f'num2: {numeral}'
        page.update()

    btn = ft.OutlinedButton(
        text= 'Adicionar',
        icon= ft.icons.ADD,
        data=0,
        on_click=contador
    )

    num = ft.Text()
    num2 = ft.Text()
    page.add(btn, num, num2)

ft.app(target=main)