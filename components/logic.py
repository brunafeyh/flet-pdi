import base64
from utils.image_processing import convert_to_grayscale_base64, apply_invert_effect_base64

def handle_upload_result(e, page, original_image, processed_image):
    if e.files:
        file = e.files[0]
        page.client_storage.set("uploaded_image_path", file.path)
        with open(file.path, "rb") as f:
            base64_str = base64.b64encode(f.read()).decode("utf-8")
            original_image.src_base64 = base64_str
            processed_image.src_base64 = None
            page.update()

def apply_technique(page, dropdown, processed_image):
    uploaded_image_path = page.client_storage.get("uploaded_image_path")
    if not uploaded_image_path or not dropdown.value:
        return

    selected = dropdown.value
    if selected == "Preto e Branco":
        result_b64 = convert_to_grayscale_base64(uploaded_image_path)
    elif selected == "Inversão de Cores":
        result_b64 = apply_invert_effect_base64(uploaded_image_path)
    else:
        result_b64 = None

    processed_image.src_base64 = result_b64
    page.update()