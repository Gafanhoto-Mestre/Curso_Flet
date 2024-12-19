"""IconButton com funcionalidade de alternância (toggle)

Crie um IconButton que funcione como um botão de alternância.
Quando clicado, alterne entre dois ícones diferentes (por exemplo, um ícone de play/pause)."""

import flet as ft
def main(page: ft.Page):
    play = False # Variável de estado

    def altera(e):
        nonlocal play # Indica que play não é uma nova variável local, e sim uma variável 'externa'.
        play = not play  # Esta linha altera a variável a cada clique, se quando for clicado o play estiver False ele altera para True, se estiver True ele altera para False, e a cada alternancia é exibido o valor de play True e play False descrito abaixo. (esta linha significa que 'not play' é o contrario de play)

        if play: # Se play for verdadeiro True, ele muda para o ícone PAUSE
            btn.icon = ft.icons.PAUSE
        else: # Se play False ele muda para o ícone PLAY, lembrado que ele inicia False, ou seja com o ícone play.
            btn.icon = ft.icons.PLAY_CIRCLE_FILL_ROUNDED

        #ou 
        # btn.icon = ft.icons.PAUSE if play else ft.icons.PLAY_CIRCLE_FILL_ROUNDED

        page.update() # atualiza a pagina/tela imediatamente (* extremamente importante isso)


    btn= ft.IconButton(
        icon= ft.icons.PLAY_CIRCLE_FILL_ROUNDED,
        on_click=altera
    )

    page.add(btn)

ft.app(target=main, view=ft.WEB_BROWSER)