import flet as ft

def main(page: ft.Page):
    page.spacing= 20
    page.theme_mode= 'light'
    page.fonts= {
        'dat': 'fonts/maquina.ttf'
    } 

    btn1= ft.ElevatedButton(text= 'Primeiro botão')
    btn2= ft.ElevatedButton(text= 'Segundo botão', disabled= True)
    btn3= ft.ElevatedButton(text= 'Terceiro botão', icon= ft.icons.SETTINGS)
    btn4= ft.ElevatedButton(text= 'Quarto botão', bgcolor= ft.colors.AMBER,
                            color= ft.colors.INDIGO,
                            icon= ft.icons.PEOPLE,
                            icon_color= ft.colors.BLACK,
                            tooltip= 'Olá, Mauro!')
    
    personalizado = ft.ButtonStyle(
        color= {
            ft.MaterialState.HOVERED: ft.colors.RED,
        },

        bgcolor= {
            ft.MaterialState.DISABLED: ft.colors.GREEN_ACCENT,
        },
        
        padding= {
            ft.MaterialState.HOVERED: 10
        },

        icon_color= {
            ft.MaterialState.HOVERED: ft.colors.AMBER
        },

        text_style= {
            ft.MaterialState.HOVERED: ft.TextStyle(font_family= 'dat')
        },

        shadow_color= 'yellow',
        surface_tint_color= "pink",
        elevation= 5




    )

    btn5= ft.ElevatedButton(text= "Personalizado", icon= ft.icons.SETTINGS,
                            style= personalizado, disabled= False)

    page.add(btn1, btn2, btn3, btn4, btn5)

ft.app(main, assets_dir= 'assets')