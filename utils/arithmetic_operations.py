import base64
import numpy as np
from PIL import Image
import io
import utils.imageUtils as imgUtils

def sum_base64(image_path1: str, image_path2: str) -> str:
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    result = image_converted_to_gray_scale1 + image_converted_to_gray_scale2

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)

    # Convertendo para base64
    buffered = io.BytesIO()
    Image.fromarray(result).save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Função para subtração de imagens
def sub_base64(image_path1: str, image_path2: str) -> str:
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    result = image_converted_to_gray_scale1 - image_converted_to_gray_scale2

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)

    # Convertendo para base64
    buffered = io.BytesIO()
    Image.fromarray(result).save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Função para multiplicação de imagens
def mul_base64(image_path1: str, image_path2: str) -> str:
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    result = image_converted_to_gray_scale1 * image_converted_to_gray_scale2

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)

    # Convertendo para base64
    buffered = io.BytesIO()
    Image.fromarray(result).save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Função para divisão de imagens
def div_base64(image_path1: str, image_path2: str) -> str:
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    epsilon = 1e-5
    safe_divisor = image_converted_to_gray_scale2 + epsilon

    result = image_converted_to_gray_scale1 / safe_divisor

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)

    # Convertendo para base64
    buffered = io.BytesIO()
    Image.fromarray(result).save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")