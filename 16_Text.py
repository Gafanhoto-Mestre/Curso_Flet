import flet as ft

def main(page: ft.Page):
    page.fonts = {
        "Drag Slayer": "Dragon Slayer.ttf",
    }
    t1 = ft.Text(
        value= 'Olá Mauro, estou percebendo que você está aprendendo flet, continue assim que você terá muito sucesso! Parabens!',
        style= ft.TextThemeStyle.DISPLAY_MEDIUM, # Tamanho da letra
        #bgcolor= ft.colors.YELLOW_400, # Cor de fundo
        color= ft.colors.RED, # Cor da letra
        font_family= 'Dragon Slayer', # Configura o estilo da fonte
        italic= True, # Coloca o texto em itálico
        #max_lines= 2, # Coloca o limite de linhas
        overflow= ft.TextOverflow.FADE, # Configura o comportamento quando a frase não cabe na tela do programa exemplo.: adiciona '...' no final
        no_wrap= False, # Se True a frase não vai ter quabra de linha
        selectable= True, # Se False, não será possível selecionar o texto
        size= 30, # Define o tamanho do texto
        text_align=ft.TextAlign.CENTER, # Define o alinhamento do texto na tela
        weight= ft.FontWeight.W_400, # Define a esperura da letra
    )
    meu_estilo = ft.TextStyle(color=ft.colors.LIGHT_BLUE_700, decoration=ft.TextDecoration.UNDERLINE, decoration_color=ft.colors.LIGHT_BLUE_700)
    
    meu_estilo2 = ft.TextStyle(
        color=ft.colors.RED, # Define a cor da letra
        bgcolor=ft.colors.AMBER, # Define a cor de fundo
        decoration= ft.TextDecoration.UNDERLINE, # Adiciona um sublinhado
        decoration_color=ft.colors.GREEN_900, # Define a cor do sublinhado
        decoration_thickness=5, # Define a espessura da linha do underline
        decoration_style=ft.TextDecorationStyle.SOLID, # Define o estilo do sublinado
        italic=True,
        size=20
        )

    # Abaixo é a configuração de texto usando o TextSapan
    t2 = ft.Text(
        spans= [
            ft.TextSpan(text='Mauro Augusto ',style=ft.TextStyle(color=ft.colors.AMBER)), # Definindo na própria linha
            ft.TextSpan(text='Januário ',style=meu_estilo, url='https://www.google.com.br/'), # Define usando uma variável
            ft.TextSpan(text='da Paixão',style=meu_estilo2) # Define usando variável
        ],
        size= 40, # Podemos configurar o tamanho da frase fora da lista
    )
    page.add(t1, t2)
ft.app(target=main, assets_dir= "assets")