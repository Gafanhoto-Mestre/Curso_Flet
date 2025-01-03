from importacoes import *

def main(page: ft.Page):
    # Centraliza o conteúdo na página
    page.update()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "DataSAM"
    page.theme_mode = "dark"

    personal = ft.ButtonStyle(
        padding={
            ft.MaterialState.HOVERED: 10
        },
        shadow_color={
            ft.MaterialState.HOVERED: 'amber',
            ft.MaterialState.FOCUSED: 'amber'
        },
        elevation={
            ft.MaterialState.HOVERED: 3,
            ft.MaterialState.FOCUSED: 3
        },
        animation_duration=250
    )

    # Cria instâncias dos campos de texto
    usuario_input = ft.TextField(
        label="Usuário",
        width=300,
        border_radius=20
    )

    senha_input = ft.TextField(
        label="Senha",
        password=True,
        width=300,
        border_radius=20,
        can_reveal_password=True
    )

    def Entrar(e):
        try:
            conexao = sqlite3.connect('Banco_interno.db')
            cursor = conexao.cursor()
            v = 'SELECT * FROM USERGERAL'
            cursor.execute(v)
            res = cursor.fetchall()
            lista_usuarios = []
            for user in res:
                dict_user_cad = {
                    "ID": user[0],
                    "NOME": user[1],
                    "USUARIO": user[2],
                    "SENHA": user[3]
                }
                lista_usuarios.append(dict_user_cad)
            
            usuario = usuario_input.value
            senha = senha_input.value

            if not usuario_input.value:
                usuario_input.error_text = 'Campo obrigatório!'
                page.update()
            if not senha_input.value:
                senha_input.error_text = 'Senha incorreta!'
                page.update()
            else:
                for valor in lista_usuarios:
                    if valor['USUARIO'] == usuario and valor['SENHA'] == senha:
                        nome = valor["NOME"]
                        abrir_navigation_drawer(nome)
                        return

        except Exception as e:
            print(f"Erro ao conectar ao banco de dados principal: {e}")
            raise

    def fechar(e):
        senha_input.value = ''
        usuario_input.value = ''
        page.clean()
        page.add(linha)
        page.update()

    def abrir_navigation_drawer(nome):
        # Função para lidar com eventos de fechamento do drawer
        def handle_dismissal(e):
            page.add(ft.Text("Usuário saiu do sistema!"))

        # Função para lidar com a seleção de itens do drawer
        def handle_change(e):
            if e.control.selected_index == 1:  # Índice do botão "Sair"
                voltar_para_pagina_inicial()

        # Função para voltar à página inicial
        def voltar_para_pagina_inicial():
            senha_input.value = ''
            usuario_input.value = ''
            page.clean()
            page.add(linha)
            page.update()
            page.close(end_drawer)

        # Cria o NavigationDrawer
        end_drawer = ft.NavigationDrawer(
            position=ft.NavigationDrawerPosition.END,
            on_dismiss=handle_dismissal,
            on_change=handle_change,
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.PERSON, label=f"Bem-vindo, {nome}"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.LOGOUT, label="Sair"
                ),
            ],
        )

        # Substitui o conteúdo da página com o drawer
        page.clean()
        page.add(
            ft.ElevatedButton(
                "Abrir menu", on_click=lambda e: page.open(end_drawer)
            )
        )
        page.update()

    linha = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(src="images/logo1.png", width=300),
                usuario_input,  # Adiciona o campo de usuário
                senha_input,    # Adiciona o campo de senha
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Entrar", width=150, icon=ft.icons.LOGIN, style=personal, on_click=Entrar),
                        ft.ElevatedButton(
                            text="Cadastrar", width=150, icon=ft.icons.PERSON_ADD, style=personal)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10  # Adiciona um espaçamento entre os botões
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente os controles dentro da coluna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza horizontalmente os controles
        ),
        alignment=ft.alignment.center
    )

    # Adiciona o container à página
    page.add(linha)

ft.app(target=main)
