import base64
import io
import numpy as np
import cv2
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils
from PIL import Image

def meanLowPassFilter(image_base64: str, kernel_size: float) -> str:
    kernel_size = int(round(kernel_size))  # Converte kernel_size para inteiro
    print(f"Tamanho do kernel: {kernel_size}")
    image = grayscale(image_base64)

    height, width = np.shape(image)

    padding = kernel_size//2

    kernel = np.ones((kernel_size, kernel_size), np.float32)

    kernel /= (kernel_size*kernel_size)

    image_mean = np.zeros((height, width), np.float32)

    padded = np.pad(image, padding, mode="edge")

    for i in range(height):
       for j in range(width):
           window = padded[i:i + kernel_size, j:j + kernel_size]
           image_mean[i, j] = imgUtils.apply_correlation(window, kernel)

    # Normaliza a imagem (se necessário)
    if imgUtils.is_normalization_necessary(image_mean):
        image_mean = imgUtils.normalize(image_mean)

    # Converte para uint8
    image_mean = imgUtils.convert_to_uint8(image_mean)

    # Converte a imagem processada para base64
    _, buffer = cv2.imencode('.jpg', image_mean)  # Codifica como .jpg
    base64_image = base64.b64encode(buffer).decode('utf-8')  # Converte a imagem para base64

    return base64_image  # Retorna a imagem processada em base64