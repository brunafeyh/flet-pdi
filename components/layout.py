import flet as ft
from components.widgets import build_upload_box
from components.widgets import build_buttons

def build_layout(page):
    original_image = ft.Image(width=300, height=150)
    processed_image = ft.Image(width=300, height=150)
    start_button_ref = ft.Ref[ft.TextButton]()
    download_button_ref = ft.Ref[ft.ElevatedButton]()

    technique_dropdown = ft.Dropdown(
        label="Técnica",
        hint_text="Selecione aqui a técnica",
        options=[
            ft.dropdown.Option("Inversão de Cores"),
            ft.dropdown.Option("Detecção de Bordas (Roberts)"),
            ft.dropdown.Option("Operador de Prewitt"),
            ft.dropdown.Option("Operador de Sobel"),
            ft.dropdown.Option("Transformação Logarítmica"),
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
        padding=10,
       
    )

    appbar = ft.Container(
        bgcolor="white",
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        content=ft.Text(
            "SISTEMA DE APLICAÇÃO DE IMAGEM  |  Disciplina de Processamento de Imagens Digitais",
            color="black",
            size=16,
            weight=ft.FontWeight.BOLD,
        ),
    )

    result_area = ft.Container(
        content=ft.Column([
            ft.Text("Resultado da Técnica", size=16),
            ft.ElevatedButton("Baixar imagem modificada", ref=download_button_ref),
            ft.Row([
                ft.Column([
                    ft.Text("Imagem Original", size=14),
                    original_image
                ], spacing=10, alignment="top"),
                ft.Column([
                    ft.Text("Imagem com Técnica Aplicada", size=14),
                    processed_image
                ], spacing=10, alignment="center"),
            ], spacing=10)
        ], spacing=10),
        padding=10,  
    )

    layout = ft.Column([
        appbar,
        ft.Row([
            upload_area,
            result_area
        ], spacing=2)
    ], spacing=2)

    return layout, file_picker, original_image, processed_image, technique_dropdown, start_button_ref, download_button_ref