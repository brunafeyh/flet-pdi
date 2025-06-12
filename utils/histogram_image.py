import base64
import io
import numpy as np
from PIL import Image, ImageDraw
import utils.imageUtils as imgUtils

def histogram_64(image_path: str) -> str:
    # Lê a imagem e converte para escala de cinza
    print('Gerando histograma...')
    original_image = imgUtils.read_image(image_path)
    image_converted_to_gray_scale = imgUtils.rgb_to_grayscale(original_image)

    # Calcula o histograma de intensidade de pixel
    hist, bins = np.histogram(image_converted_to_gray_scale.flatten(), bins=256, range=(0, 256))

    # Normaliza o histograma para ajustar ao tamanho da imagem
    max_hist_value = max(hist)
    if max_hist_value > 0:
        hist = [int(x * 255 / max_hist_value) for x in hist]

    # Cria a imagem do histograma manualmente
    hist_img = Image.new('L', (256, 256), color=255)  # 'L' para escala de cinza
    draw = ImageDraw.Draw(hist_img)

    # Desenha as barras do histograma
    for x in range(256):
        # O valor máximo do histograma é o tamanho da barra (em Y)
        draw.line([(x, 255), (x, 255 - hist[x])], fill=0)  # Cor preta (histograma)

    # Salva o gráfico em um objeto de memória (BytesIO)
    buffered = io.BytesIO()
    hist_img.save(buffered, format="PNG")
    buffered.seek(0)

    # Converte a imagem em memória para base64
    base64_histogram = base64.b64encode(buffered.read()).decode("utf-8")

    return base64_histogram  # Retorna a imagem do histograma em base64
