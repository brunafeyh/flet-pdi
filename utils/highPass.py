import base64
import io
import numpy as np
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils
import cv2

def highPassFilter(image_path: str, kernel: np.ndarray) -> str:
    """
    Aplica um filtro passa-alta em uma imagem usando o kernel fornecido e retorna a imagem em base64.
    """
    # Carrega e converte a imagem para escala de cinza
    image = grayscale(image_path)

    height, width = image.shape
    kernel_size = kernel.shape[0]
    padding = kernel_size // 2

    # Aplica o preenchimento nas bordas da imagem
    padded = np.pad(image, padding, mode='edge')

    # Inicializa a imagem de saída
    image_highPass = np.zeros((height, width), np.float32)

    # Aplica a correlação com o kernel
    for i in range(height):
        for j in range(width):
            window = padded[i:i+kernel_size, j:j+kernel_size]
            image_highPass[i, j] = imgUtils.apply_correlation(window, kernel)

    # Normaliza a imagem, se necessário
    if imgUtils.is_normalization_necessary(image_highPass):
        image_highPass = imgUtils.normalize(image_highPass)

    # Converte para uint8 para ser compatível com a codificação em imagem
    image_highPass = imgUtils.convert_to_uint8(image_highPass)

    # Codifica a imagem para PNG em memória (BytesIO)
    _, buffer = cv2.imencode(".png", image_highPass)  # Usando imencode para codificar a imagem no formato PNG

    # Converte para base64
    base64_image = base64.b64encode(buffer).decode("utf-8")

    return base64_image
