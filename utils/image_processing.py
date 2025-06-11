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