"""3. Formulário com Validação
Objetivo: Desenvolva um pequeno formulário com um campo de texto, um TextButton para enviar, e um PopupMenuButton com opções de validação ("Verificar Se Está Vazio", "Verificar Se Tem Números").
Dica: Dependendo da opção selecionada no menu, o TextButton deve realizar a validação e exibir uma mensagem adequada."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 400
    page.window.height = 400
    page.window.center()


    def validacao(e):
        opcao = e.control.text
        informacao = escreva.value

        if opcao == 'Verificar se está vazio':
            if informacao.strip() == "":
                resultado.value = 'O campo está vazio!'
            else:
                resultado.value = 'O campo contém texto!'

        elif opcao == "Verificar se tem números":
            if any(char.isdigit() for char in informacao):
                resultado.value = 'O campo contém números!'
            else:   
                resultado.value = 'O campo nãp contém números!'

        page.update()

    #Criação do campo texto    
    escreva = ft.TextField(label= 'Digite algo:')

    #Criação do PopupMenuButton com validação
    menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text= 'Verificar se está vazio', on_click= validacao),
            ft.PopupMenuItem(text= 'Verificar se tem números', on_click= validacao)
        ]
    )

    botao_validacao = ft.TextButton(text= 'Validar')

    #Criação do Text para exibir o resultado
    resultado = ft.Text(value= "O resultado da validação aparecerá aqui")

    page.add(escreva, menu, botao_validacao, resultado)
ft.app(target= main)