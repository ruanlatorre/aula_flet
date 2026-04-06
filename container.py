import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Cotainer com padding, margin e border"),
            bgcolor=ft.Colors.BLUE,
            padding=20,
            margin=15,
            border=ft.Border(
                top=ft.BorderSide(1, ft.Colors.BLACK),
                bottom=ft.BorderSide(1, ft.Colors.BLACK),
                left=ft.BorderSide(1, ft.Colors.BLACK),
                right=ft.BorderSide(1, ft.Colors.BLACK),
            ),
            border_radius=10,
            width=300,
            height=100
        )
    )


ft.run(main)
