import flet as ft
def main(page: ft.Page):

    # Aspect Radio
    # 9:16      0.56
    # 2:3       0.66
    # 1:1       1.0
    # 16:9      1.77

    grid = ft.GridView(
        controls= [ft.Image(src= f'https://picsum.photos/250/300?{num}',fit= 'cover') for num in range(20)],
        runs_count= 3, # quantidade de itens por linha
        padding= 20, # largura das laterais 
        spacing= 20, # largura do espassamento entre as linhas
        run_spacing= 20, # largura do espassamento entre as colunas
        # max_extent= 100, # Define o tamanho maximo dos elementos, fica responsivo e se adapta ao tamanho do aplicativo.
        expand= True, # Se habilitado o scroll tbm será habilitado. 
        # height= 300, # Se definido, scroll tbm é habilitado.
        auto_scroll= True, # desce até o final da página.
        child_aspect_ratio= 0.66

    )

    page.add(grid)
ft.app(target= main)