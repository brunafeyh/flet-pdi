import base64
import io
import numpy as np
from algorithms.highPassFilter import highPassFilter
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils
import cv2

def highBoostFilter(image_path: str, kernel: np.ndarray, alpha: float) -> str:
    """
    Aplica um filtro de alta frequência reforçado (high boost) em uma imagem
    e retorna a imagem em base64.
    """
    # Carrega e converte a imagem para escala de cinza
    image = grayscale(image_path)

    # Aplica o filtro de alta frequência
    image_highPass = highPassFilter(image_path, kernel)

    # Aplica o efeito de high boost
    image_boost = alpha * image_highPass + image

    # Normaliza a imagem, se necessário
    if imgUtils.is_normalization_necessary(image_boost):
        image_boost = imgUtils.normalize(image_boost)

    # Converte a imagem para uint8 para ser compatível com a codificação em imagem
    image_boost = imgUtils.convert_to_uint8(image_boost)

    # Codifica a imagem para PNG em memória (BytesIO)
    _, buffer = cv2.imencode(".png", image_boost)  # Usando imencode para codificar a imagem no formato PNG

    # Converte para base64
    base64_image = base64.b64encode(buffer).decode("utf-8")

    return base64_image
