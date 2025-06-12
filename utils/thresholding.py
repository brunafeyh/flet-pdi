import cv2
import numpy as np
import base64
import utils.imageUtils as imgUtils

def thresholding(image_path: str, threshold: int) -> str:
    # Lê a imagem e converte para escala de cinza
    original_image = imgUtils.read_image(image_path)
    gray = imgUtils.rgb_to_grayscale(original_image)

    height, width = gray.shape

    # Inicializa uma imagem binária (preta e branca)
    binary_image = np.zeros((height, width), np.float32)

    # Aplica o thresholding (limiarização)
    for i in range(height):
        for j in range(width):
            if gray[i, j] > threshold:
                binary_image[i, j] = 255
            else:
                binary_image[i, j] = 0

    # Converte para uint8
    binary_image = imgUtils.convert_to_uint8(binary_image)

    # Codifica a imagem binária para o formato PNG em memória (sem salvar no disco)
    _, buffer = cv2.imencode('.png', binary_image)  # Codifica a imagem em PNG

    # Converte o buffer em base64
    base64_image = base64.b64encode(buffer).decode("utf-8")

    return base64_image  # Retorna a imagem como base64