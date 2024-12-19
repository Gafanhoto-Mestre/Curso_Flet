import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()

    linha1 = ft.Row(controls = [
            ft.OutlinedButton(text= '1'),
            ft.OutlinedButton(text= '2'),
            ft.OutlinedButton(text= '3'),
            ft.OutlinedButton(text= '4')
        ],
        #wrap= True, # Habilita a quebra de linha
        spacing = 5  # Define o espaço entre os elementos
        # alignment= ft.MainAxisAlignment.CENTER # Centraliza tudo que tem na linha
    )

    page.add(linha1)
ft.app(target= main)