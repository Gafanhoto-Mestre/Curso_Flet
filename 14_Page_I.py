import flet as ft
def main(page: ft.Page):
    page.bgcolor = ''
    page.bgcolor = "#f12f12"
    page.bgcolor = ft.colors.AMBER

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  #Alinhamento horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento vertical
    page.padding = 50 #largura da margem de todos os lados
    page.spacing = 20 #ditancia de uma linha para outra
    page.title = 'DATASAM v.4.0.5' #Adiciona título a tela do programa!

    #page.padding = ft.padding.all()
    #page.padding = ft.padding.all(100)
    #page.padding = ft.padding.symmetric(vertical=10, horizontal=50)
    #page.padding = ft.padding.only(top=, left=, right=, bottom=)

    page.add(
        ft.Text(value='Digite seu nome: '),
        ft.Container(ft.Text(value="Digite seu nome:"), bgcolor="Red"),
        ft.Container(ft.Text(value="Digite seu nome:"), bgcolor="Red")
    )

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)