import flet as ft

# Breakpoint    Dimensão
# xs            < 576 px
# sm            >= 576 px
# md            >= 768 px
# lg            >= 992 px
# xl            >= 1200 px
# xxl           >= 1400 px

def main(page: ft.Page):
    page.window.width = 700
    page.window.height= 400
    page.window.center()

    rrow = ft.ResponsiveRow(
        columns=12,
        run_spacing= 50,
        spacing= 30,
        expand= True,
        controls=[
            ft.ElevatedButton(
                col={"sm": 4, "md": 3, "lg": 2, "xl": 1},
                text= 'Botão 1',
                bgcolor= ft.colors.AMBER,
                color= ft.colors.BLACK
            ),
            ft.ElevatedButton(
                col={"sm": 4, "md": 3, "lg": 2, "xl": 1},
                text= 'Botão 2',
                bgcolor= ft.colors.AMBER,
                color= ft.colors.BLACK
            ),
            ft.ElevatedButton(
                col={"sm": 4, "md": 3, "lg": 2, "xl": 1},
                text= 'Botão 3',
                bgcolor= ft.colors.AMBER,
                color= ft.colors.BLACK
            ),
        ]
    )

    text = ft.Text()

    def page_size(e):
        text.value = f'Largura: {page.window.width}, Altura: {page.window.height}'
        text.update()

    page.on_resize = page_size

    page.add(rrow, text)
ft.app(target= main)