import base64
from utils.image_processing import apply_roberts_base64, apply_prewitt_base64, apply_sobel_base64, apply_log_base64
from utils.histogram import histogram
from utils.equalized_histogram import equalize_histogram
from utils.arithmetic_operations import mul_base64, sub_base64, sum_base64, div_base64
from utils.invert_effect import apply_invert_effect_base64
from utils.gray_scale import grayscale

def handle_upload_result(e, page, original_image, original_image_b, processed_image, key):
    # Verifica se o arquivo foi enviado
    if e.files:
        file = e.files[0]
        page.client_storage.set(key, file.path)  # Armazena o caminho do arquivo

        # Converte o arquivo para base64 e exibe na imagem original
        with open(file.path, "rb") as f:
            base64_str = base64.b64encode(f.read()).decode("utf-8")
            if key == "uploaded_image_path":
                original_image.src_base64 = base64_str
            elif key == "uploaded_image_path_b":
                original_image_b.src_base64 = base64_str

            # Limpa a imagem processada
            processed_image.src_base64 = None
            page.update()

def apply_technique(page, dropdown, processed_image):
    image_a_path = page.client_storage.get("uploaded_image_path")
    image_b_path = page.client_storage.get("uploaded_image_path_b")  # Novo caminho para a segunda imagem

    selected = dropdown.value
    if not image_a_path or not selected:
        return

    if selected == "Inversão de Cores":
        result_b64 = apply_invert_effect_base64(image_a_path)
    elif selected == "Detecção de Bordas (Roberts)":
        result_b64 = apply_roberts_base64(image_a_path)
    elif selected == "Escala de Cinza":
        result_b64 = grayscale(image_a_path)
    elif selected == "Operador de Prewitt":
        result_b64 = apply_prewitt_base64(image_a_path)
    elif selected == "Operador de Sobel":
        result_b64 = apply_sobel_base64(image_a_path)
    elif selected == "Transformação Logarítmica":
        result_b64 = apply_log_base64(image_a_path)
    elif selected == "Histograma (Escala de cinza)":
        result_b64 = histogram(image_a_path)
    elif selected == "Equalização de Histograma":
        result_b64 = equalize_histogram(image_a_path)
    elif selected == "Multiplicação de Imagens" and image_b_path:
        # Verifica se a Imagem B está carregada
        if image_b_path:
            result_b64 = mul_base64(image_a_path, image_b_path)  # Multiplicação de Imagens
        else:
            result_b64 = None
    elif selected == "Adição de Imagens" and image_b_path:
        # Verifica se a Imagem B está carregada
        if image_b_path:
            result_b64 = sum_base64(image_a_path, image_b_path)  # Adição de Imagens
        else:
            result_b64 = None
    elif selected == "Subtração de Imagens" and image_b_path:
        # Verifica se a Imagem B está carregada
        if image_b_path:
            result_b64 = sub_base64(image_a_path, image_b_path)  # Subtração de Imagens
        else:
            result_b64 = None
    elif selected == "Divisão de Imagens" and image_b_path:
        # Verifica se a Imagem B está carregada
        if image_b_path:
            result_b64 = div_base64(image_a_path, image_b_path)  # Divisão de Imagens
        else:
            result_b64 = None
    else:
        result_b64 = None

    # Atualizar a imagem processada com o resultado em base64
    processed_image.src_base64 = result_b64
    page.update()  # Atualiza a página após aplicar a técnica
