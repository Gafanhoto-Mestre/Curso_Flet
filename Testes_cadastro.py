import flet as ft
def main(page: ft.Page):
    page.bgcolor= ft.colors.AMBER
    page.title= 'Navegações'
    page.window.height= 700
    page.window.width= 430
    page.window.maximizable= False
    page.vertical_alignment= "center"
    page.horizontal_alignment= "center"

    def btn_principal(e):
        stack.controls.clear()
        page.update()

        stack.controls.append(_main)
        stack.update()

    def btn_editar(e):
        stack.controls.clear()
        page.update()

        stack.controls.append(Editar)
        stack.update()

    def btn_pesquisar(e):
        stack.controls.clear()
        page.update()

        stack.controls.append(pesquisar)
        stack.update()

    page.floating_action_button= ft.FloatingActionButton(icon= ft.icons.ADD, bgcolor= ft.colors.LIGHT_BLUE, on_click= btn_principal)
    page.floating_action_button_location= ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar= ft.BottomAppBar(
        bgcolor= ft.colors.SURFACE_VARIANT,
        shape= ft.NotchShape.CIRCULAR,
        content= ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.WHITE, on_click= btn_editar),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, on_click= btn_pesquisar),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.WHITE),
                ft.IconButton(icon=ft.Icons.SHARE, icon_color=ft.Colors.WHITE),
            ]
        ),
    )

    #conteiner principal
    _main= ft.Container(
        width= 400,
        height= 560,
        bgcolor= ft.colors.RED_300,
        border_radius= ft.border_radius.vertical(top=16, bottom=16),
        alignment= ft.alignment.center,
        shadow= ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.7, color="black")),
        content= ft.Text(value= "Inicio", size= 32),
        
    )

    #Editar
    Editar= ft.Container(
        width= 400,
        height= 560,
        bgcolor= ft.colors.RED_300,
        border_radius= ft.border_radius.vertical(top=16, bottom=16),
        alignment= ft.alignment.center,
        shadow= ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.7, color="black")),
        content= ft.Text(value= "Editar", size= 32)
    )


    #Pesquisar
    pesquisar= ft.Container(
        width= 400,
        height= 560,
        bgcolor= ft.colors.RED_300,
        border_radius= ft.border_radius.vertical(top=16, bottom=16),
        alignment= ft.alignment.center,
        shadow= ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.7, color="black")),
        content= ft.Text(value= "Pesquisar", size= 32)
    )

    #Configuarar
    config= ft.Container(
        width= 400,
        height= 560,
        bgcolor= ft.colors.RED_300,
        border_radius= ft.border_radius.vertical(top=16, bottom=16),
        alignment= ft.alignment.center,
        shadow= ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.7, color="black")),
        content= ft.Text(value= "Configurar", size= 32)
    )

    #Pesquisar
    compartilhar= ft.Container(
        width= 400,
        height= 560,
        bgcolor= ft.colors.RED_300,
        border_radius= ft.border_radius.vertical(top=16, bottom=16),
        alignment= ft.alignment.center,
        shadow= ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.7, color="black")),
        content= ft.Text(value= "Compartilhar", size= 32)
    )

    #stack principal
    stack= ft.Stack(
        controls=[
            _main
        ]
    )
    
    

    page.add(stack)

ft.app(main)