import flet as ft
from components.widgets import build_upload_box
from components.widgets import build_buttons

def build_layout(page):
    original_image = ft.Image(width=350, height=350)
    processed_image = ft.Image(width=350, height=350, fit=ft.ImageFit.CONTAIN)
    start_button_ref = ft.Ref[ft.TextButton]()
    download_button_ref = ft.Ref[ft.ElevatedButton]()

    technique_dropdown = ft.Dropdown(
        label="Técnica",
        hint_text="Selecione aqui a técnica",
        options=[
            ft.dropdown.Option("Preto e Branco"),
            ft.dropdown.Option("Inversão de Cores"),
        ],
        width=300,
    )

    file_picker = ft.FilePicker()
    upload_box = build_upload_box(file_picker)
    buttons = build_buttons(start_button_ref)

    upload_area = ft.Container(
        content=ft.Column([
            technique_dropdown,
            upload_box,
            buttons
        ], spacing=20),
        padding=20,
        expand=True
    )

    appbar = ft.Container(
        bgcolor="black",
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        content=ft.Text(
            "SISTEMA DE APLICAÇÃO DE IMAGEM  |  Disciplina de Processamento de Imagens Digitais",
            color="white",
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
        expand=True
    )

    result_area = ft.Container(
        content=ft.Column([
            ft.Text("Resultado da Técnica", size=16),
            ft.ElevatedButton("Baixar imagem modificada", ref=download_button_ref),
            ft.Row([
                ft.Column([
                    ft.Text("Imagem Original", size=14),
                    original_image
                ], spacing=5, alignment="center"),
                ft.Column([
                    ft.Text("Imagem com Técnica Aplicada", size=14),
                    processed_image
                ], spacing=5, alignment="center"),
            ], alignment="spaceEvenly", spacing=30)
        ], spacing=10),
        padding=20,
        expand=True
    )

    layout = ft.Column([
        appbar,
        ft.Row([
            upload_area,
            ft.VerticalDivider(width=1),
            result_area
        ], spacing=30, expand=True)
    ], spacing=20, expand=True)

    return layout, file_picker, original_image, processed_image, technique_dropdown, start_button_ref, download_button_ref