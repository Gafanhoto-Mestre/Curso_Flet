import flet as ft


def main(page: ft.Page):
    page.title = "Exemplo de diálogos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def confirmar_alerta(e):
        page.close(alerta)
        page.add(ft.Text(f"Ação disparada!: {e.control.text}"))

    alerta = ft.AlertDialog(
        modal=True,
        title=ft.Text("Fechar DataSAM?"),
        content=ft.Text("Confirma?"),
        actions=[
            ft.TextButton("Sim", on_click= confirmar_alerta),
        ],
    )

    page.add(
        ft.ElevatedButton("Opções de diálogo!", on_click=lambda e: page.open(dlg_modal)),
    )


ft.app(main)