import flet as ft


def main(page: ft.Page):
    # Configurações da Janela
    page.title = "Gamer Card"
    page.bgcolor = "1E1E1E"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cabeçalho: Avatar (Emoji) e Nome do Lado
    cabecalho = ft.Row(
        controls=[
            ft.Text("👨🏻‍💻", size=60),  # Emoji a prova de erros
            ft.Column(
                controls=[
                    ft.Text("oxyruan", size=24,
                            weight="bold", color="white"),
                    ft.Text("Nível 999 - The Best Hacker",
                            size=24, color="grey300"),
                ],
                spacing=2,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Status: Barra de HP, MP e XP
    status_bar = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(
                    "HP: 999", text_align=ft.TextAlign.CENTER, weight="bold"
                ),
                bgcolor="red400",
                border_radius=10,
                padding=8,
                expand=3,
            ),
            ft.Container(
                content=ft.Text(
                    "MP: 999", text_align=ft.TextAlign.CENTER, weight="bold"
                ),
                bgcolor="amber400",
                border_radius=10,
                padding=8,
                expand=2,
            ),
            ft.Container(
                content=ft.Text(
                    "Aura: 10000", text_align=ft.TextAlign.CENTER, weight="bold"
                ),
                bgcolor="blue400",
                border_radius=10,
                padding=8,
                expand=2,
            ),
        ],
        spacing=10

    )

    # Botões: Ações do Jogador
    botoes = ft.Row(
        controls=[
            ft.Button("Enviar Mensagem",
                      bgcolor="#36628E",
                      color="white"
                      ),

            ft.Button("Atacar",
                      bgcolor="red",
                      color="white"
                      ),

            ft.Button("Defender",
                      bgcolor="green",
                      color="white"
                      ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Cartão Final
    cartao = ft.Container(
        content=ft.Column(
            controls=[
                cabecalho,
                status_bar,
                botoes,
            ],
            spacing=30,
        ),
        bgcolor="#2E2E2E",
        padding=40,
        border_radius=20,
        width=450,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="black"  # Aqui vai ser um efeito de sombra
        ),

    )

    page.add(cartao)


ft.run(main)
