import base64
import io
import numpy as np
import cv2
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils
from PIL import Image

def meanLowPassFilter(image_base64: str, kernel_size: int) -> str:
    # Converte a imagem de base64 para uma imagem que pode ser processada
    img_data = base64.b64decode(image_base64)
    img = Image.open(io.BytesIO(img_data))
    image = np.array(img.convert('L'))  # Converte para escala de cinza

    height, width = np.shape(image)

    padding = kernel_size // 2

    # Cria o kernel de média
    kernel = np.ones((kernel_size, kernel_size), np.float32)
    kernel /= (kernel_size * kernel_size)

    image_mean = np.zeros((height, width), np.float32)

    # Aplica o padding
    padded = np.pad(image, padding, mode="edge")

    # Aplicando o filtro de média (convolução)
    for i in range(height):
        for j in range(width):
            window = padded[i:i + kernel_size, j:j + kernel_size]
            image_mean[i, j] = imgUtils.apply_correlation(window, kernel)

    # Normaliza a imagem (se necessário)
    if imgUtils.is_normalization_necessary(image_mean):
        image_mean = imgUtils.normalize(image_mean)

    # Converte para uint8
    image_mean = imgUtils.convert_to_uint8(image_mean)

    # Converte a imagem para base64
    _, buffer = cv2.imencode('.jpg', image_mean)
    base64_image = base64.b64encode(buffer).decode('utf-8')

    return base64_image  # Retorna a imagem em base64