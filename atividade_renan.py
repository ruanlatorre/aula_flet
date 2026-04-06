import flet as ft


def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "Tobirama"

    # Texto para feedback
    mensagem = ft.Text(
        "Quem criou a técinica chamada 'Hiraishin'?",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "✅"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "❌"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não é o {imagem_correta}. Tente de novo."

        container_minato.on_click = None
        container_tobirama.on_click = None

        btn_jogar_novamente.visible = True

        page.update()

    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = "Quem criou a técnica chamada 'Hiraishin'?"

        container_minato.image.opacity = 1.0
        container_minato.on_click = jogar
        container_minato.content.size = 0
        container_minato.content.value = "Minato"
        container_minato.bgcolor = ft.Colors.GREY_200

        container_tobirama.image.opacity = 1.0
        container_tobirama.on_click = jogar
        container_tobirama.content.size = 0
        container_tobirama.content.value = "Tobirama"
        container_tobirama.bgcolor = ft.Colors.GREY_200

        page.update()

    # Container MINATO
    container_minato = ft.Container(
        content=ft.Text(
            "Minato",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/minato.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container TOBIRAMA
    container_tobirama = ft.Container(
        content=ft.Text(
            "Tobirama",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/tobirama.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Selecione a imagem certa",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_minato,
                        container_tobirama
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )


ft.run(main)
