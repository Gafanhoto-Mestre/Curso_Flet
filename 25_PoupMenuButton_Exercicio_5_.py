"""Exercício 5: Menu de ações em uma lista de itens
Crie uma lista de itens onde cada item tem um PopupMenuButton associado com opções como "Editar", "Deletar".
Ao selecionar uma opção, execute a ação correspondente (por exemplo, editar o texto do item ou remover o item da lista)."""

import flet as ft

def main(page: ft.Page):
    items = []

    def add_item(e):
        item = novo_item.value
        if item:
            item_row = ft.Row([
                ft.Text(value=item),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Editar", on_click=lambda e: edit_item(e, item_row)),
                        ft.PopupMenuItem(text="Deletar", on_click=lambda e: delete_item(e, item_row))
                    ]
                )
            ])
            items.append(item_row)
            item_da_lista.controls.append(item_row)
            novo_item.value = ""
            page.update()

    def edit_item(e, item_row):
        item_text = item_row.controls[0]
        novo_texto = input("Novo texto do item:")
        if novo_texto:
            item_text.value = novo_texto
            page.update()

    def delete_item(e, item_row):
        items.remove(item_row)
        item_da_lista.controls.remove(item_row)
        page.update()

    novo_item = ft.TextField(hint_text="Novo item")
    botao_adicionar = ft.OutlinedButton(text="Adicionar", on_click=add_item)
    item_da_lista = ft.Column()

    page.add(novo_item, botao_adicionar, item_da_lista)

ft.app(target=main)