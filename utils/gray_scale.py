import base64
import numpy as np
import cv2
import io
import utils.imageUtils as imgUtils
from PIL import Image

def grayscale(image_path: str) -> str:
    # Lê a imagem original
    image = imgUtils.read_image(image_path)
    
    height, width = image.shape[:2]
    image_gray = np.zeros((height, width), np.float32)

    # Converte a imagem para escala de cinza usando a fórmula de luminosidade
    for i in range(height):
        for j in range(width):
            B, G, R = image[i, j]
            image_gray[i, j] = int(0.114 * B + 0.587 * G + 0.299 * R)

    # Converte para tipo uint8 (intervalo de 0 a 255)
    image_gray = imgUtils.convert_to_uint8(image_gray)

    # Salva a imagem em memória (sem salvar no disco)
    buffered = io.BytesIO()
    Image.fromarray(image_gray).save(buffered, format="PNG")
    
    # Converte para base64
    base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return base64_image
