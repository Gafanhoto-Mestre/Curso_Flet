"""Exercício 4: Menu de configuração de perfil
Crie um PopupMenuButton com opções como "Alterar Nome", "Alterar Senha", "Excluir Conta".
Ao selecionar uma opção, exiba um formulário apropriado (por exemplo, um campo de texto para alterar o nome)."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height= 400
    page.window.center()

    def escolha(e):
        op = e.control.text
        if op == 'Alterar nome':
            a.visible = True
            b.visible = False
            c.visible = False
            
        elif op == "Alterar senha":
            a.visible = False
            b.visible = True
            c.visible = False
            
        elif op == 'Excluir conta':
            a.visible = False
            b.visible = False
            c.visible = True
            
        page.update()

    def excluido(e):
        e.control.on_click
        a.visible = False
        b.visible = False
        c.visible = False
        d.value = "Conta Excluída!"
        page.add(d)
        page.update()

    opcoes = [
        ft.PopupMenuItem(text= 'Alterar nome', on_click= escolha), 
        ft.PopupMenuItem(text= 'Alterar senha', on_click= escolha),
        ft.PopupMenuItem(text= 'Excluir conta', on_click= escolha)
        ]
    menu = ft.PopupMenuButton(items=opcoes)

    a = ft.TextField(label="Nome", width=200, visible= False)
    b = ft.TextField(label= "Senha",width=200, visible= False, password= True)
    c = ft.ElevatedButton(text= "Confirmar Exclusão", on_click= excluido,visible= False)
    d = ft.Text()

    page.add(menu, a, b, c, d)
ft.app(target= main)