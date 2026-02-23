import flet as ft
# IMPORTA A BIBLIOTECA E APELIDA ELA (ALIAS)

def main(page: ft.Page):
    page.title = "Meu primeiro App Flet" #Define o titulo da janela
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text("Bem-vindo(a) ao meu App"),
        ft.Text("Aqui você pode criar o que quiser!")
    )
ft.run(main)
