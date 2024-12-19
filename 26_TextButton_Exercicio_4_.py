"""4. Controle de Tema (Claro/Escuro)
Objetivo: Crie um TextButton que altera o tema da aplicação entre claro e escuro. Use um PopupMenuButton com as opções "Tema Claro" e "Tema Escuro" para definir o tema inicial.
Dica: Use variáveis para armazenar o estado atual do tema e ajuste as cores da interface com base nele."""

import flet as ft

def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()
    
    # Variável para armazenar o estado atual do tema
    is_dark_mode = False

    # Função para aplicar o tema
    def apply_theme():
        page.theme_mode = "dark" if is_dark_mode else "light"
        page.update()

    # Função para alternar o tema ao clicar no TextButton
    def toggle_theme(e):
        nonlocal is_dark_mode
        is_dark_mode = not is_dark_mode
        apply_theme()

    # Função para definir o tema inicial ao selecionar uma opção no PopupMenuButton
    def set_initial_theme(e):
        nonlocal is_dark_mode
        if e.control.text == "Tema Escuro":
            is_dark_mode = True
        else:
            is_dark_mode = False
        apply_theme()

    # Criação do PopupMenuButton para definir o tema inicial
    theme_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Tema Claro", on_click=set_initial_theme),
            ft.PopupMenuItem(text="Tema Escuro", on_click=set_initial_theme)
        ]
    )

    # Criação do TextButton para alternar o tema
    theme_button = ft.OutlinedButton(text="Alternar Tema", on_click=toggle_theme)

    # Adicionar os componentes à página
    page.add(theme_menu, theme_button)

# Inicia a aplicação
ft.app(target=main)