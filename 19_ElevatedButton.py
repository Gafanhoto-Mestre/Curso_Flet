import flet as ft

def main(page: ft.Page):
    page.window.width = 400 # Largura da JANELA DO PROGRAMA
    page.window.height = 500 # Altura da JANELA DO PROGRAMA
    page.spacing=30 # Adiciona espaço entre os elementos
    page.scroll= True
    botao1 = ft.ElevatedButton(
        text='Clique aqui!')
    
    botao2= ft.ElevatedButton(
        text='Botão inativo',
        disabled=True) # Desabilitando o botão
    
    botao3 = ft.ElevatedButton(
        text='Entrar',
        icon=ft.icons.LOGIN) # Adicionando ícones
    
    botao4= ft.ElevatedButton(
        text='Botão persolanizado',
        bgcolor=ft.colors.AMBER, 
        color=ft.colors.BLACK,
        icon= ft.icons.VIEW_AGENDA, 
        icon_color=ft.colors.BLUE,
        tooltip='Exibe um texto ao passar o mouse!',
        url='www.uol.com')
    
    meu_estilo = ft.ButtonStyle(
        color={
            ft.MaterialState.DEFAULT: ft.colors.BLACK, # Cor da letra quando botão está em estado normal
            ft.MaterialState.HOVERED: ft.colors.RED, # Cor do texto quando mouse passa em cima
        },
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.AMBER, # Cor de fundo quando mouse passa por cima
            ft.MaterialState.DEFAULT: ft.colors.LIGHT_BLUE_600, # Cor de fundo no estado normal
            ft.MaterialState.DISABLED: ft.colors.GREY, # Cor do botão quando estiver desabilitado
            ft.MaterialState.FOCUSED: ft.colors.GREEN, # Cor de fundo quando botão está em foco, usando o TAB
        },
        padding={
                ft.MaterialState.HOVERED: 20,
                ft.MaterialState.DEFAULT: 10,
        },
        animation_duration=1000, # Define a duração da animação do botão (quando passa o mouse, quando o botão fica em foco...)
        side={
            ft.MaterialState.HOVERED: ft.BorderSide(width=5, color=ft.colors.RED), # Define cor da borda ao passar o mouse
            ft.MaterialState.DEFAULT: ft.BorderSide(width=5, color=ft.colors.ORANGE), # Define cor da borda
        },
        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=5), # Define o formato do botão
            #ft.MaterialState.DEFAULT: ft.StadiumBorder(), # Botão no formato padrão
            #ft.MaterialState.DEFAULT: ft.CircleBorder(), # Botão em formato de círculo
            #ft.MaterialState.DEFAULT: ft.BeveledRectangleBorder(radius=10), # Botão com as bordas cortadas
            ft.MaterialState.DEFAULT: ft.ContinuousRectangleBorder(radius=10) # Botão com botão arredondado
        },
    )
    botao5 = ft.ElevatedButton(text='Botão estilizado', style=meu_estilo)
    page.add(botao1, botao2, botao3,botao4, botao5)

    def button_cliced(e):
        if hasattr(page, "img"):
            page.remove(page.img)
            del page.img
        else:
            if not hasattr(page, "img"):
                page.img = ft.Image(src='images/redenova.png', width=50, height=50)
                page.add(page.img)
            botao6.data += 1
            botao6.update()
        botao6.data += 1
        botao6.update()
     
    page.textoo = ft.Text(value='Para apagar!!')

    page.add(page.textoo)

    def apag(e):
        if hasattr(page, "textoo"):
            page.remove(page.textoo)
            del page.textoo
        bt_apag.update()

    bt_apag = ft.ElevatedButton(text="apagar texto", on_click=apag)   

    botao6 = ft.ElevatedButton(
        text='Acionar imagem',
        on_click=button_cliced, 
        data=0)
    
    page.add(botao6, bt_apag)
ft.app(target=main)