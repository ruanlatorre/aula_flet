
from pydantic import color
import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Image(
            src="images/paisagem-foda.jpg",
            width=300,
            height=400
        ),
        ft.Container(
            content=ft.Text("Paisagem - Ghost of Tsushima",
                            color=ft.Colors.WHITE, size=32),
            image=ft.DecorationImage(
                src="images/paisagem-foda.jpg",
                fit=ft.BoxFit.COVER
            ),
            bgcolor=ft.Colors.BLUE,
            width=400,
            height=400,
            alignment=ft.Alignment(0, 0)
        )
    )


ft.run(main)
