import flet as ft


def main(page: ft.Page):
    page.bgcolor = "gray"

    def mostrar_mensagem(e):
        page.add(ft.Text("Welcome to the world of Cyber Security!"))

    page.add(
        ft.Image(src="images/redteste.png", height=150),
        ft.Button(
            content="Click here to explore Security Offensive",
            on_click=mostrar_mensagem,
        ),
    )


ft.run(main)
