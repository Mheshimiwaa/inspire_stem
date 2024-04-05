import flet as ft


def main(page : ft.Page):
    page.title = "Learning FLET"
    content = ft.Column(
        spacing= 20, 
        controls=[ 
        ft.Text("This is a sample flet application", size= 32 ,weight = "w600"), 
        ft.Text("Welcome to learning flet",size=16),
        ft.Row(
            spacing=20,
            controls=[
                ft.Text("This is a row in flet"),
                ft.ElevatedButton("Click Me!")
             ]
          )
       ],
    )

    #DISPLAY SCREEN
    page.add(content)

ft.app(target=main)
    
