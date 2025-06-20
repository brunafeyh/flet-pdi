import flet as ft
from components.layout import build_layout
from components.logic import handle_upload_result, apply_technique

def main(page: ft.Page):
    page.title = "Sistema de Aplicação de Imagem"
    page.scroll = "auto"
    page.client_storage.clear()

    # Variáveis globais para armazenar os valores de entrada
    numeric_value = ft.Ref[ft.TextField]()  # Para o valor numérico
    boost_intensity_value = ft.Ref[ft.TextField]()  # Para a intensidade de reforço

    # Função de clique para o botão "Iniciar"
    def on_start_button_click(e):
        print("Botão Iniciar clicado")  # Depuração

        # Acessa os valores inseridos
        numeric_input_value = numeric_value.current.value
        boost_intensity = boost_intensity_value.current.value

        print(f"Valor numérico inserido: {numeric_input_value}")  # Exibe o valor numérico
        print(f"Intensidade de reforço inserida: {boost_intensity}")  # Exibe a intensidade de reforço

        # Passando os valores para a função apply_technique
        apply_technique(page, technique_dropdown, processed_image, numeric_input_value, boost_intensity)
        page.update()  # Atualiza a página após aplicar a técnica

    # Função de clique para o botão "Baixar"
    def download_image(e):
        base64_str = processed_image.src_base64
        if base64_str:
            page.launch_url(f"data:image/png;base64,{base64_str}")

    # Criando os botões diretamente no main
    start_button = ft.TextButton("Iniciar", on_click=on_start_button_click)
    download_button = ft.ElevatedButton("Baixar Imagem", on_click=download_image)

    # Adicionando os botões lado a lado
    button_row = ft.Row([start_button, download_button], spacing=10)

    # Criando os campos de entrada
    numeric_input = ft.TextField(ref=numeric_value, label="Valor Numérico", keyboard_type=ft.KeyboardType.NUMBER)
    boost_intensity_input = ft.TextField(ref=boost_intensity_value, label="Intensidade de Reforço", keyboard_type=ft.KeyboardType.NUMBER)

    # Layout dos inputs (colocando-os no topo)
    top_layout = ft.Column([numeric_input, boost_intensity_input], spacing=10)

    # Adicionando os botões e os campos de entrada à página
    page.add(top_layout)
    page.add(button_row)

    # Construção do layout (sem o botão)
    layout, file_picker_a, file_picker_b, original_image, original_image_b, processed_image, technique_dropdown, start_button_ref, download_button_ref = build_layout(page)

    page.overlay.append(file_picker_a)
    page.overlay.append(file_picker_b)

    # Manipulação de resultados do upload de arquivos
    file_picker_a.on_result = lambda e: handle_upload_result(e, page, original_image, original_image_b, processed_image, key="uploaded_image_path")
    file_picker_b.on_result = lambda e: handle_upload_result(e, page, original_image, original_image_b, processed_image, key="uploaded_image_path_b")

    # Adicionando o layout à página
    page.add(layout)

# Executa a aplicação
ft.app(target=main)
