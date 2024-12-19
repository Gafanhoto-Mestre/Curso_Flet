"""Exercício 3: Container com Background de Imagem
Crie um Container que utiliza uma imagem como fundo. Dentro do container, adicione um botão que, ao ser clicado, exibe um texto sobre a imagem. Garanta que o texto esteja legível sobre a imagem.
Dicas:
Use a propriedade background_image.
Certifique-se de que o botão e o texto sejam claramente visíveis, ajustando as cores conforme necessário."""

import flet as ft
def main(page: ft.Page):
    page.window.width= 600
    page.window.height= 600
    page.window.center()

    # Cria um container para texto invisível
    texto_no_container= ft.Container(
        content= ft.Text(
            "Texto sobre a imagem!",
            size=24,
            color= ft.colors.AMBER,
            text_align= ft.TextAlign.CENTER,
        ),
        visible= False,
        padding= ft.padding.symmetric(vertical=10, horizontal= 5),
        border_radius= 20,
        alignment= ft.alignment.center
    )

    # Criar o botão do texto
    botao= ft.ElevatedButton(
        text= "Clique para mostrar o texto",
        on_click= "",
        color= ft.colors.LIGHT_BLUE_600
    )

    # Cria um container com imagem de fundo
    container_principal= ft.Container(
        content= ft.Column(
            [botao, texto_no_container],
            alignment= ft.MainAxisAlignment.END,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ),
        width= page.window_width,
        height= 300,
        image_src= 'images/user.png',
        image_fit= ft.ImageFit.COVER,
        
    )


    page.add(container_principal)
ft.app(target= main)