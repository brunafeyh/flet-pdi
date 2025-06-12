import base64
from utils.image_processing import apply_roberts_base64, apply_prewitt_base64, apply_sobel_base64, apply_log_base64
from utils.equalized_histogram import equalize_histogram
from utils.arithmetic_operations import mul_base64, sub_base64, sum_base64, div_base64
from utils.invert_effect import apply_invert_effect_base64
from utils.gray_scale import grayscale
from utils.histogram_image import histogram_64
from utils.thresholding import thresholding
from utils.mean_loss_pass import meanLowPassFilter
from utils.median_low_pass import medianLowPassFilter
from utils.array import parse_kernel
from utils.highPass import highPassFilter
from utils.high_Boost_pass import highBoostFilter

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

def apply_technique(page, dropdown, processed_image, numeric_value=None, boost_intensity=None):
    # Exibe o valor numérico recebido para depuração
    print(f"Valor numérico recebido: {numeric_value}") 
    print(f"Valor intensidade recebido: {boost_intensity}") 
    

    image_a_path = page.client_storage.get("uploaded_image_path")
    image_b_path = page.client_storage.get("uploaded_image_path_b")  # Novo caminho para a segunda imagem

    selected = dropdown.value
    if not image_a_path or not selected:
        return

    if selected == "Inversão de Cores":
        result_b64 = apply_invert_effect_base64(image_a_path)
    elif selected == "Passa-Alta básico":
        array = parse_kernel(numeric_value)
        print('Mariz - ', array)
        result_b64 = highPassFilter(image_a_path, array)
    elif selected == "Passa-Alta Alto Reforço":
        array = parse_kernel(numeric_value)
        print('Matriz - ', array)
        print(boost_intensity)
        
        # Pegando o valor do campo numérico
        numeric_input_value = boost_intensity  # Isso pega o valor diretamente da referência do Flet
        
        try:
            numeric_input_value = float(numeric_input_value.strip())  # Tente converter, removendo espaços extras
            print(f"Valor numérico recebido: {numeric_input_value}")  # Exibe o valor numérico como número
        except ValueError:
            try:
                numeric_input_value = int(numeric_input_value.strip())  # Tente converter para inteiro se o float falhar
                print(f"Valor inteiro recebido: {numeric_input_value}")  # Exibe o valor como inteiro
            except ValueError:
                print("O valor inserido não é um número válido.")  # Caso o valor não seja nem float nem int
                return  # Retorna e não aplica a técnica se o valor não for válido
        result_b64 = highBoostFilter(image_a_path, array, numeric_input_value)
    elif selected == "Detecção de Bordas (Roberts)":
        result_b64 = apply_roberts_base64(image_a_path)
    elif selected == "Limiarização (Threshold)":
        try:
            # Converte o valor para número (inteiro ou flutuante)
            numeric_input_value = float(numeric_value)
            print(f"Valor numérico recebido: {numeric_input_value}")  # Exibe o valor numérico como número
        except ValueError:
            print("O valor inserido não é um número válido.")  # Caso não seja um número válido
            return  # Retorna e não aplica a técnica se o valor não for válido
        result_b64 = thresholding(image_a_path, numeric_input_value)
    elif selected == "Passa-Baixa Média (Básico)":
        try:
            # Converte o valor para número (inteiro ou flutuante)
            numeric_input_value = float(numeric_value)
            print(f"Valor numérico recebido: {numeric_input_value}")  # Exibe o valor numérico como número
        except ValueError:
            print("O valor inserido não é um número válido.")  # Caso não seja um número válido
            return  # Retorna e não aplica a técnica se o valor não for válido
        result_b64 = meanLowPassFilter(image_a_path, numeric_input_value)
    elif selected == "Passa-Baixa Mediana":
        try:
            # Converte o valor para número (inteiro ou flutuante)
            numeric_input_value = float(numeric_value)
            print(f"Valor numérico recebido: {numeric_input_value}")  # Exibe o valor numérico como número
        except ValueError:
            print("O valor inserido não é um número válido.")  # Caso não seja um número válido
            return  # Retorna e não aplica a técnica se o valor não for válido
        result_b64 = medianLowPassFilter(image_a_path, numeric_input_value)
    elif selected == "Escala de Cinza":
        result_b64 = grayscale(image_a_path)
    elif selected == "Operador de Prewitt":
        result_b64 = apply_prewitt_base64(image_a_path)
    elif selected == "Operador de Sobel":
        result_b64 = apply_sobel_base64(image_a_path)
    elif selected == "Transformação Logarítmica":
        result_b64 = apply_log_base64(image_a_path)
    elif selected == "Histograma (Escala de cinza)":
        result_b64 = histogram_64(image_a_path)
    elif selected == "Equalização de Histograma":
        result_b64 = equalize_histogram(image_a_path)
    elif selected == "Multiplicação de Imagens" and image_b_path:
        if image_b_path:
            result_b64 = mul_base64(image_a_path, image_b_path)
        else:
            result_b64 = None
    elif selected == "Adição de Imagens" and image_b_path:
        if image_b_path:
            result_b64 = sum_base64(image_a_path, image_b_path)
        else:
            result_b64 = None
    elif selected == "Subtração de Imagens" and image_b_path:
        if image_b_path:
            result_b64 = sub_base64(image_a_path, image_b_path)
        else:
            result_b64 = None
    elif selected == "Divisão de Imagens" and image_b_path:
        if image_b_path:
            result_b64 = div_base64(image_a_path, image_b_path)
        else:
            result_b64 = None
    else:
        result_b64 = None

    processed_image.src_base64 = result_b64
    page.update()  # Atualiza a página após aplicar a técnica
