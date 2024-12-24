import flet as ft
def main(page: ft.Page):
    page.bgcolor = ''
    page.bgcolor = "#f12f12"
    page.bgcolor = ft.colors.AMBER

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  #Alinhamento horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinhamento vertical


    page.padding = 50 #largura da margem de todos os lados
    #ou
    #page.padding = ft.padding.all() 
    #page.padding = ft.padding.all(100)

    page.spacing = 20 #ditancia de uma linha para outra
    page.title = 'DATASAM v.4.0.5' #Adiciona título a tela do programa!

    #page.padding = ft.padding.symmetric(vertical=10, horizontal=50)
    #page.padding = ft.padding.only(top=, left=, right=, bottom=)


    page.window_title_bar_hidden = False # Permite remover a barra de título (por padrão fica False)
    page.window_always_on_top = False # Permite que o programa fique sempre em primeiro plano (por padrão fica False)
    page.window_frameless = False # Componente para remover os botões de minimizar, maximizar e fechar da janela
    page.window_full_screen = False # Componente que permite iniciar o aplicativo em tela cheia (esta opção desabilita as opções de minimizar e fechar na janela)
    page.window.height = 400 # Permite definir a altura da janela do programa
    page.window.width = 400 # Permite definir a largura da janela do programa
    # page.window.max_height = 400 # Permite definir a altura máxima da janela do programa
    # page.window.min_height = 300# Permite definir a altura mínima da janela do programa
    # page.window.max_width = 400 # Permite definir a largura máximada janela do programa
    # page.window.min_width = 300 # Permite definir a largura mínima da janela do programa
    page.window.resizable = True # Permite desativar o redimencionamento da tela do programa (por padrão fica True)
    page.window_top = 150 # Permite definir a distancia da janela de cima para baixo
    page.window_left = 560 # Permite definir a distancia da janela da esquerda para a direita
    page.window_movable= True # Se ficar como False o usuário não consiguirá mover a janela do programa
    
    page.window.prevent_close = False # Se ficar como "True" a opção de fechar a janela no canto superior da janela fica sem ação, isso serve para adicionar um evento antes que o usuário feche a janela.

    # page.window.progress_bar = 1 # Permite adicionar uma barra de progresso no ícone do programa
    # print(page.platform) # Permite informar qual sistema o programa está sendo executado


    """def redimencionei(e):
        tamanho = page.window_width
        if tamanho > 400.0:
            page.bgcolor = ft.colors.BLUE_GREY_600
            page.update()
        else:
            page.bgcolor = ft.colors.AMBER
            page.update()
        print(f'Tamanho: {tamanho}')
    
    page.on_resize = redimencionei # Evento que, associado a uma função permite realizar uma ação se necessário como troca de imagens, alterar cor, dentre outras, de acordo com as dimensões da janela 
    
    """

    # def descricao_evento(e):
    #     print(e.data)
    #     match e.data:
    #         case 'moved':
    #             print('Moveu a página!')
    #         case 'resized':
    #             print('Alterou tamanho!')
    #         case 'minimize':
    #             print('Mininimou o programa!')
    #         case 'unmaximize':
    #             print('Voltou para tela normal')
    #         case 'blur':
    #             print('Perdeu o foco!')

    #         case _:
    #             print('Outra ação!')

    # page.on_window_event = descricao_evento



    page.add(
        ft.Text(value='Digite seu nome: '),
        ft.Container(ft.Text(value="Digite seu nome:"), bgcolor="Red"),
        ft.Container(ft.Text(value="Digite seu nome:"), bgcolor="Red")
    )

    page.update()


ft.app(target=main)