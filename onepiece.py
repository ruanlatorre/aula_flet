import flet as ft


def main(page: ft.Page):
    page.bgcolor = "purple"
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Eu vou ser rei dos piratas.")
        )
    page.add(
        ft.Text("Olá, meu nome é Luffy!"),
        ft.Image(
            src="images/luffy.webp", height=150
        ),
        
        ft.Button(
            content="Clique aqui",
            on_click=mostrar_mensagem
        )
    )

ft.run(main)
