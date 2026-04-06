import flet as ft


def main(page: ft.Page):

    def mostrar_mensagem(e):
        page.add(
            ft.Text(f"Clicou no container!")
        )

    def mostrar_transparente(e):
        page.add(
            ft.Text(f"Clicou no container transparente!")
        )

    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text("Container não clicável"),
                    bgcolor=ft.Colors.AMBER,
                    padding=10,
                    margin=10,
                    border_radius=10,
                    width=150,
                    height=150,
                    alignment=ft.Alignment(0, 0)

                ),

                ft.Container(
                    content=ft.Text("Container clicável"),
                    bgcolor=ft.Colors.GREEN_200,
                    padding=10,
                    margin=10,
                    border_radius=10,
                    width=150,
                    height=150,
                    alignment=ft.Alignment(0, 0),
                    on_click=mostrar_mensagem
                ),

                ft.Container(
                    content=ft.Text("Container clicável: Transparente"),
                    bgcolor=ft.Colors.TRANSPARENT,
                    padding=10,
                    margin=10,
                    border_radius=10,
                    width=150,
                    height=150,
                    alignment=ft.Alignment(0, 0),
                    on_click=mostrar_transparente
                )
            ],
            scroll=ft.ScrollMode.ALWAYS
        )
    )


ft.run(main)
