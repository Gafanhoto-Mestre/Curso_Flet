import flet as ft

def main(page: ft.Page):
    # page.window.width= 700
    # page.window.height = 400
    # page.window.center()
    page.bgcolor= "#cff2c7"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Alinha componentes no meio do aplicativo na vertical
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER # Alinha componentes no meio do aplicativo na horizontal

    container = ft.Container(
        height= 400, # Altura do container
        width= 400, # Largura do container 

        # expand= True,
        bgcolor= "#cff2c7",
        image_src= 'images/user.png',

        # margin= ft.margin.all(20), 
        # margin= ft.margin.only(top=10,bottom=30,left=40,right=50),
        # margin= ft.margin.symmetric(vertical=20,horizontal=40),
   
        # border= ft.border.all(width=10, color= ft.colors.RED) #Define uma borda,
        # border= ft.border.only(
        #     top= ft.BorderSide(width=10, color= ft.colors.RED),
        #     left= ft.BorderSide(width=10, color= ft.colors.GREEN),
        #     right= ft.BorderSide(width=10, color= ft.colors.BLUE),
        #     bottom= ft.BorderSide(width=10, color= ft.colors.YELLOW))

        # border= ft.border.symmetric(
        #     vertical= ft.BorderSide(width= 10, color= ft.colors.RED),
        #     horizontal= ft.BorderSide(width= 10, color= ft.colors.YELLOW))

        # border_radius= ft.border_radius.all(10)   # Não funciona se a borda estiver sendo personalizada!,
        # border_radius= ft.border_radius.horizontal(10),
        # border_radius= ft.border_radius.vertical(10),
        # border_radius= ft.border_radius.only(top_left=10, bottom_right=10, top_right=0, bottom_left=0)

        content= ft.Row(
            controls= [
                ft.ElevatedButton(text= 'Texto 1'),
                ft.ElevatedButton(text= 'Texto 2'),
                ft.ElevatedButton(text= 'Texto 3'),
                ft.ElevatedButton(text= 'Texto 4'),
            ],
            # alignment= ft.MainAxisAlignment.END
        ),
        
        # padding= ft.padding.all(20),
        # padding= ft.padding.symmetric(vertical=6, horizontal=20),
        # padding= ft.padding.only(left= 100, bottom= 200,right= 20, top= 10),


        # content= ft.Text(value= "testando!", color= ft.colors.BLACK, size= 30),
        alignment= ft.alignment.center,

        # shape= ft.BoxShape.CIRCLE
        # shape= ft.BoxShape.RECTANGLE # Padrão
        
        gradient= ft.LinearGradient(
            begin= ft.alignment.top_center,
            end= ft.alignment.bottom_center,
            colors= [ft.colors.GREEN, ft.colors.BLUE]
        ),

        # SOMBRA / DESFOQUE COM 1 COR DE SOMBRA
        # shadow= ft.BoxShadow(
        #     spread_radius= 0, # Espessura da borda (espassamento antes de aplicar a sombra de desfoque)
        #     blur_radius= 40, # Espesura do desfoque da borda
        #     # color= ft.colors.BLUE # Define a cor da sombra
        #     # blur_style= ft.ShadowBlurStyle.INNER # Define o defoque para dentro do container
        #     # blur_style= ft.ShadowBlurStyle.NORMAL # Define o defoque dentro e fora do container
        #     blur_style= ft.ShadowBlurStyle.NORMAL, # Padrão
        #     offset= ft.Offset(x=-10, y=20)

        # SOMBRA / COM 2 CORES
        shadow= [ft.BoxShadow(
            spread_radius= 10, # Espessura da borda (espassamento antes de aplicar a sombra de desfoque)
            blur_radius= 0, # Espesura do desfoque da borda
            color= ft.colors.BLUE, # Define a cor da sombra
            # blur_style= ft.ShadowBlurStyle.INNER # Define o defoque para dentro do container
            # blur_style= ft.ShadowBlurStyle.NORMAL # Define o defoque dentro e fora do container
            blur_style= ft.ShadowBlurStyle.NORMAL, # Padrão
            offset= ft.Offset(x=-10, y=-20)
            ),
            ft.BoxShadow(
                spread_radius= 10, # Espessura da borda (espassamento antes de aplicar a sombra de desfoque)
            blur_radius= 0, # Espesura do desfoque da borda
            color= ft.colors.RED, # Define a cor da sombra
            # blur_style= ft.ShadowBlurStyle.INNER # Define o defoque para dentro do container
            # blur_style= ft.ShadowBlurStyle.NORMAL # Define o defoque dentro e fora do container
            blur_style= ft.ShadowBlurStyle.NORMAL, # Padrão
            offset= ft.Offset(x=-20, y=-40)
            ),
        ]
    )


    page.add(container)
ft.app(target=main)

