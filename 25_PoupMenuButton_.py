import flet as ft
def main(page: ft.Page):
    page.window.width= 300
    page.window.height= 300
    page.window.center()

    def consultar(e):
        print('Consultar paciente')

    def cadastrar(e):
        print('Cadastrar paciente')

    def configurar(e):
        print('Configurações')

    def checando(e):
        e.control.checked = not e.control.checked
        e.control.update()

    pb = ft.PopupMenuButton(
        icon= ft.icons.LIST,
        items=[
            ft.PopupMenuItem(icon= ft.icons.MENU_BOOK,text="Cadastrar Paciente", on_click=cadastrar),
            ft.PopupMenuItem(icon= ft.icons.SEARCH,text= "Consultar Paciente", on_click= consultar),
            ft.PopupMenuItem(), # Sem parametro ele exibe uma linha
            ft.PopupMenuItem(icon= ft.icons.SETTINGS,text= "Configurações", on_click= configurar),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(
                text= 'Selecione esse item',
                checked= False,
                on_click= checando
            )
        ]
    )
    page.add(pb)
ft.app(target=main)