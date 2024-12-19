import flet as ft

def main(page: ft.Page):
    # img = ft.Image(
    #     src= 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png',
    #     #border_radius= 50, # Define o arredondamento das bordas

    #     #border_radius= ft.border_radius.all(20)  # Define o arredondamento das bordas

    #     #border_radius=ft.border_radius.horizontal(left=10, right=40) #Define somente as bordas horizontais de direita e esquerda

    #     #border_radius= ft.border_radius.vertical(top=10, bottom=40) # Define somente as bordas de cima e de baixo

    #     #border_radius= ft.border_radius.only(top_left=10,top_right=10,bottom_left=30, bottom_right=40) # Define o tamanho de cada borda

    #     # height=1000, # Define o tamanho da altura (fixa)

    #     # width= 400, # Define a largura da figura (fixa)

    #     # fit= ft.ImageFit.FIT_HEIGHT # Preenche a altura total da janela

    #     # fit= ft.ImageFit.FIT_WIDTH # Preeche a largura da janela

    #     fit= ft.ImageFit.COVER

    img2 = ft.Image(src="images/slogan.png")

    page.add(img2)

ft.app(target=main, assets_dir='assets')