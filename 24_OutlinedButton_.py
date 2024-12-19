import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height= 300

    estilo = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.GREEN
        },
        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10)
        },
    )

    btn = ft.OutlinedButton(
        text="Primeiro OutlinedButton",
        icon= ft.icons.ZOOM_IN,
        icon_color= ft.colors.AMBER_800,
        tooltip='Tooltip',
        url='https://avatars.githubusercontent.com/u/102273996?s=280&v=4',
        style= estilo
        )
    
    page.add(btn)
ft.app(target=main)