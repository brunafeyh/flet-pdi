import base64
import numpy as np
from PIL import Image
import io
import cv2
import utils.imageUtils as imgUtils

def convert_to_grayscale_base64(image_path: str) -> str:
    with Image.open(image_path).convert("RGB") as img:
        np_img = np.array(img)
        gray = np.mean(np_img, axis=2).astype(np.uint8)
        gray_img = Image.fromarray(gray)
        buffered = io.BytesIO()
        gray_img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

def apply_invert_effect_base64(image_path: str) -> str:
    with Image.open(image_path).convert("RGB") as img:
        np_img = np.array(img)
        inverted = 255 - np_img
        inverted_img = Image.fromarray(inverted)
        buffered = io.BytesIO()
        inverted_img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

def apply_roberts_base64(image_path: str) -> str:
    original_image = imgUtils.read_image(image_path)
    gray = imgUtils.rgb_to_grayscale(original_image)

    height, width = gray.shape

    kernel_x = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    kernel_y = np.array([[1, 0], [0, -1]], dtype=np.float32)

    grad_x = np.zeros_like(gray, dtype=np.float32)
    grad_y = np.zeros_like(gray, dtype=np.float32)

    for i in range(height - 1):
        for j in range(width - 1):
            region = gray[i:i+2, j:j+2]
            grad_x[i, j] = imgUtils.apply_correlation(region, kernel_x)
            grad_y[i, j] = imgUtils.apply_correlation(region, kernel_y)

    magnitude = np.sqrt(grad_x**2 + grad_y**2)

    if imgUtils.is_normalization_necessary(magnitude):
        magnitude = imgUtils.normalize(magnitude)

    magnitude = imgUtils.convert_to_uint8(magnitude)

    _, buffer = cv2.imencode(".png", magnitude)
    return base64.b64encode(buffer).decode("utf-8")

def apply_prewitt_base64(image_path: str) -> str:
    original_image = imgUtils.read_image(image_path)
    gray = imgUtils.rgb_to_grayscale(original_image)

    kernel_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_y = np.array([
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ], dtype=np.float32)

    height, width = gray.shape
    grad_x = np.zeros_like(gray, dtype=np.float32)
    grad_y = np.zeros_like(gray, dtype=np.float32)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            region = gray[i-1:i+2, j-1:j+2]
            grad_x[i, j] = imgUtils.apply_correlation(region, kernel_x)
            grad_y[i, j] = imgUtils.apply_correlation(region, kernel_y)

    magnitude = np.sqrt(grad_x**2 + grad_y**2)

    if imgUtils.is_normalization_necessary(magnitude):
        print('Normalização necessária!')
        magnitude = imgUtils.normalize(magnitude)

    magnitude = imgUtils.convert_to_uint8(magnitude)

    _, buffer = cv2.imencode(".png", magnitude)
    return base64.b64encode(buffer).decode("utf-8")

def apply_sobel_base64(image_path: str) -> str:
    original_image = imgUtils.read_image(image_path)
    gray = imgUtils.rgb_to_grayscale(original_image)

    kernel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_y = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ], dtype=np.float32)

    height, width = gray.shape
    grad_x = np.zeros_like(gray, dtype=np.float32)
    grad_y = np.zeros_like(gray, dtype=np.float32)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            region = gray[i-1:i+2, j-1:j+2]
            grad_x[i, j] = imgUtils.apply_correlation(region, kernel_x)
            grad_y[i, j] = imgUtils.apply_correlation(region, kernel_y)

    magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)

    if imgUtils.is_normalization_necessary(magnitude):
        magnitude = imgUtils.normalize(magnitude)

    magnitude = imgUtils.convert_to_uint8(magnitude)

    _, buffer = cv2.imencode(".png", magnitude)
    return base64.b64encode(buffer).decode("utf-8")

def apply_log_base64(image_path: str) -> str:
    original_image = imgUtils.read_image(image_path)
    gray = imgUtils.rgb_to_grayscale(original_image)
    image_float = gray.astype(np.float32)

    c = 255 / np.log(1 + np.max(image_float))
    log_image = c * np.log(1 + image_float)

    if imgUtils.is_normalization_necessary(log_image):
        log_image = imgUtils.normalize(log_image)

    log_image = imgUtils.convert_to_uint8(log_image)

    _, buffer = cv2.imencode(".png", log_image)
    return base64.b64encode(buffer).decode("utf-8")


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