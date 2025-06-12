import flet as ft
from components.widgets import build_upload_box
from components.widgets import build_buttons

def build_layout(page):
    original_image = ft.Image(width=300, height=150)
    original_image_b = ft.Image(width=300, height=150)  # Segunda imagem
    processed_image = ft.Image(width=300, height=150)

    start_button_ref = ft.Ref[ft.TextButton]()  # Referência do botão
    download_button_ref = ft.Ref[ft.ElevatedButton]()

    print(f"start_button_ref no build_layout: {start_button_ref}")  # Verifique se a referência está correta

    technique_dropdown = ft.Dropdown(
        label="Técnica",
        hint_text="Selecione aqui a técnica",
        options=[
            ft.dropdown.Option("Escala de Cinza"),
            ft.dropdown.Option("Inversão de Cores"),
            ft.dropdown.Option("Detecção de Bordas (Roberts)"),
            ft.dropdown.Option("Operador de Prewitt"),
            ft.dropdown.Option("Operador de Sobel"),
            ft.dropdown.Option("Transformação Logarítmica"),
            ft.dropdown.Option("Multiplicação de Imagens"),
            ft.dropdown.Option("Adição de Imagens"),
            ft.dropdown.Option("Subtração de Imagens"),
            ft.dropdown.Option("Divisão de Imagens"),
            ft.dropdown.Option("Histograma (Escala de cinza)"),
            ft.dropdown.Option("Equalização de Histograma"),
        ],
        width=300,
    )

    file_picker_a = ft.FilePicker()
    file_picker_b = ft.FilePicker()  # Segunda imagem para a multiplicação
    upload_box_a = build_upload_box(file_picker_a, label="Imagem A")
    upload_box_b = build_upload_box(file_picker_b, label="Imagem B")  # Caixa de upload para a segunda imagem

    #buttons = build_buttons(start_button_ref)

    # Container condicional para a segunda imagem
    image_b_container = ft.Container(upload_box_b, visible=False)

    def on_dropdown_change(e):
        # Atualizar visibilidade da Imagem B com base na seleção do dropdown
        if technique_dropdown.value in ["Multiplicação de Imagens", "Adição de Imagens", "Subtração de Imagens", "Divisão de Imagens"]:
            image_b_container.visible = True
        else:
            image_b_container.visible = False
        result_area.content.controls[1].visible = image_b_container.visible  # Exibe ou oculta a Imagem B
        page.update()

    technique_dropdown.on_change = on_dropdown_change

    upload_area = ft.Container(
        content=ft.Column([
            technique_dropdown,
            upload_box_a,
            image_b_container,
            
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
                    ft.Text("Imagem A", size=14),
                    original_image
                ], spacing=10, alignment="top"),
                ft.Column([
                    ft.Text("Imagem B", size=14),
                    original_image_b
                ], spacing=10, alignment="top", visible=False),  # Só mostra se for Multiplicação
                ft.Column([
                    ft.Text("Imagem com Técnica Aplicada", size=14),
                    processed_image
                ], spacing=10, alignment="center"),
            ], spacing=10)
        ], spacing=10),
        padding=10,
    )

    def update_visibility_on_multiplication():
        is_mult = technique_dropdown.value in ["Multiplicação de Imagens", "Adição de Imagens", "Subtração de Imagens", "Divisão de Imagens"]
        # Acessando corretamente a coluna da imagem B e atualizando a visibilidade
        result_area.content.controls[2].controls[1].visible = is_mult  # Imagem B
        page.update()

    technique_dropdown.on_change = lambda e: [on_dropdown_change(e), update_visibility_on_multiplication()]

    layout = ft.Column([
        appbar,
        ft.Row([
            upload_area,
            result_area
        ], spacing=2)
    ], spacing=2)

    return layout, file_picker_a, file_picker_b, original_image, original_image_b, processed_image, technique_dropdown, start_button_ref, download_button_ref
