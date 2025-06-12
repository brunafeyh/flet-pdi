import base64
import io
import matplotlib.pyplot as plt
import numpy as np
import utils.imageUtils as imgUtils

def histogram(image_path: str) -> str:
    # Lê a imagem e converte para escala de cinza
    original_image = imgUtils.read_image(image_path)
    image_converted_to_gray_scale = imgUtils.rgb_to_grayscale(original_image)

    # Inicializa o histograma com 256 bins (um para cada valor de pixel de 0 a 255)
    h = [0] * 256

    # Calcula o histograma de intensidade de pixel
    height, width = image_converted_to_gray_scale.shape
    for img_line in range(1, height):
        for img_column in range(1, width):
            h[image_converted_to_gray_scale[img_line, img_column]] += 1

    # Gera o gráfico de histograma usando Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(range(256), h, color='gray')
    plt.title('Histograma de Intensidade de Pixel')
    plt.xlabel('Intensidade de Pixel (0-255)')
    plt.ylabel('Número de Pixels')
    plt.xlim([-5, 260])
    plt.grid(axis='y', alpha=0.75)

    # Salva o gráfico em um objeto de memória (BytesIO)
    buffered = io.BytesIO()
    plt.savefig(buffered, format="png")
    plt.close()  # Fecha o gráfico para liberar recursos

    # Converte a imagem em memória para base64
    buffered.seek(0)
    base64_histogram = base64.b64encode(buffered.read()).decode("utf-8")

    return base64_histogram
