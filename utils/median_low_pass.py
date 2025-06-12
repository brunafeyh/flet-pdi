import base64
import io
import numpy as np
import cv2
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils
from PIL import Image

def medianLowPassFilter(image_base64: str, kernel_size: int) -> str:
    # Converte a imagem de base64 para uma imagem que pode ser processada
    img_data = base64.b64decode(image_base64)
    img = Image.open(io.BytesIO(img_data))
    image = np.array(img.convert('L'))  # Converte para escala de cinza

    height, width = np.shape(image)

    padding = kernel_size // 2

    image_median = np.zeros((height, width), np.float32)

    # Aplica o padding
    padded = np.pad(image, padding, mode="edge")

    # Aplica o filtro de mediana (convolução)
    for i in range(height):
        for j in range(width):
            window = padded[i:i + kernel_size, j:j + kernel_size]
            image_median[i, j] = np.median(window)

    # Normaliza a imagem (se necessário)
    if imgUtils.is_normalization_necessary(image_median):
        image_median = imgUtils.normalize(image_median)

    # Converte para uint8
    image_median = imgUtils.convert_to_uint8(image_median)

    # Converte a imagem para base64
    _, buffer = cv2.imencode('.jpg', image_median)
    base64_image = base64.b64encode(buffer).decode('utf-8')

    return base64_image  # Retorna a imagem em base64
