import base64
import io
import numpy as np
import cv2
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils
from PIL import Image

def medianLowPassFilter(image_base64: str, kernel_size: float) -> str:
    kernel_size = int(round(kernel_size))  # Converte kernel_size para inteiro
    print(f"Tamanho do kernel: {kernel_size}")
    image = grayscale(image_base64)

    height, width = np.shape(image)

    padding = kernel_size // 2

    image_median = np.zeros((height, width), np.float32)

    padded = np.pad(image, padding, mode="edge")

    for i in range(height):
        for j in range(width):
            window = padded[i:i + kernel_size, j:j + kernel_size]
            image_median[i, j] = np.median(window)

    if imgUtils.is_normalization_necessary(image_median):
        image_median = imgUtils.normalize(image_median)

    image_median = imgUtils.convert_to_uint8(image_median)

    # Converte a imagem processada para base64
    _, buffer = cv2.imencode('.jpg', image_median)  # Codifica como .jpg
    base64_image = base64.b64encode(buffer).decode('utf-8')  # Converte a imagem para base64

    return base64_image  # Retorna a imagem processada em base64