import flet as ft
from flet import Page


def main(page: Page):
    page.title="Menu principal"
    page.window_height = 800
    page.window_width = 1000
    page.window_center()
    
    page.add(
        ft.ElevatedButton(text= "traductor" , width=150,height=100),
        #ft.ElevatedButton("Disabled button", disable= True),
    )
ft.app(main)