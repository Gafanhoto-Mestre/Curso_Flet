# 20_FilledButoon (ft.FilledButton)

import flet as ft

def main(page: ft.Page):
    botao1 = ft.FilledButton(
        text= 'Botão 1')
    
    botao2 = ft.FilledButton(
        text='Botão com ícone',
        icon= ft.icons.DELETE,
        icon_color= ft.colors.RED,
            )

    estilo = ft.ButtonStyle(
        padding=50,
        #padding= ft.padding.all()
        #padding= ft.padding.only(left=, right=,top=,bottom=),
        #padding= ft.padding.symmetric(),
        animation_duration=1000,
        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.RED),
            ft.MaterialState.HOVERED: ft.BorderSide(10,ft.colors.GREEN),
        },
        #shape= ft.RoundedRectangleBorder(radius=0), # Define o formato para todos os estados
        shape={
            ft.MaterialState.HOVERED: ft.CircleBorder(), # Eu quiser definir um estado como (HOVERED, DEFAULT, DESABLED...) usamos as chaves { }
        },)
    
    botao3 = ft.FilledButton(
        text='Botão customizado',
        icon= ft.icons.SETTINGS,
        style= estilo)

    botao4 = ft.FilledButton(
            text='Botão com link',
            url='www.google.com',
            tooltip='Clique aqui para printar!')
    
    def printar(e):
        print('Printado')

    botao5= ft.FilledButton(text='Tirar print', on_click=printar)

    botao_semtexto = ft.FilledButton(icon="delete", icon_color="red", text=" ")

    page.add(botao1, botao2, botao3, botao3, botao4, botao5, botao_semtexto)
ft.app(target=main)