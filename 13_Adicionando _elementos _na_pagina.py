#  13_Adicionando_elementos_na_pagina #

import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text(value='Olá, Mauro vc está aprendendo Flet!')
    page.add(mensagem)
    #ou
    page.add(ft.Text(value="Segunda linha!"))
    #ou
    page.add(ft.Text(value='Palavra 1'), ft.Text(value='Palavra 2'))
    #ou
    elementos = [
        ft.Text(value='Mauro 1'),
        ft.Text(value='Mauro 2'),
        ft.Text(value='Mauro 3'),
    ]
    page.add(*elementos) # O asterísco indica que a página irá adicionar todos os elementos

ft.app(target=main)