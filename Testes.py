import flet as ft
def main(page: ft.Page):
    container= ft.Container(
        # height= 300,
        # padding= 100,
        bgcolor= ft.colors.AMBER,
        expand= True,
        image_src= 'https://flet.dev/img/docs/controls/container/container-diagram.png',

        # O COMPONENTE "margin" funciona como se fosse o padding para o container
        # margin= ft.margin.all(10)
        # margin= ft.margin.only(top=10, bottom=10)
        # margin= ft.margin.symmetric(vertical=50, horizontal=10)

        #border= ft.border.all(20, color= ft.colors.RED)

        border_radius= ft.border_radius.all(50)
    
    )


    page.add(container)
ft.app(target=main)

