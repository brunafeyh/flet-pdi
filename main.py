import flet as ft
from components.layout import build_layout
from components.logic import handle_upload_result, apply_technique

def main(page: ft.Page):
    page.title = "Sistema de Aplicação de Imagem"
    page.scroll = "auto"
    page.client_storage.clear()

    layout, file_picker, original_image, processed_image, technique_dropdown, start_button_ref, download_button_ref = build_layout(page)

    page.overlay.append(file_picker)

    file_picker.on_result = lambda e: handle_upload_result(e, page, original_image, processed_image)
    start_button_ref.current.on_click = lambda e: apply_technique(page, technique_dropdown, processed_image)

    def download_image(e):
        base64_str = processed_image.src_base64
        if base64_str:
            page.launch_url(f"data:image/png;base64,{base64_str}")

    download_button_ref.current.on_click = download_image

    page.add(layout)

ft.app(target=main)