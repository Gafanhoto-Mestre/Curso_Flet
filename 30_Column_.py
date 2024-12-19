import flet as ft
def main(page: ft.Page):
    page.window.width= 600
    page.window.height= 500
    page.window.center()
    page.scroll= True

    botns= [
        ft.ElevatedButton(text= "Logar"),
        ft.ElevatedButton(text= "Cancelar")
    ]

    linha_btns= ft.Row(controls= botns)
    
    col1 = ft.Column(
        scroll=True,
        expand= True,
        spacing= 20,
        controls=[
            ft.TextField(label= "Usuário:", width= 200, height=40, text_size= 14),
            ft.TextField(label= "Senha", width= 200, height=40, password= True),
            linha_btns
        ],
        alignment= ft.MainAxisAlignment.CENTER
    )

    img = ft.Image(src= "images/opacidade26.png", width=100)



    linha = ft.ResponsiveRow(
        expand= True,
        controls=[
            ft.Container(img, bgcolor= "#72916a"),
            ft.Container(col1, bgcolor= "#72916a"),
        ],
        alignment= ft.MainAxisAlignment.CENTER
    )

    page.add(linha)
ft.app(target= main)