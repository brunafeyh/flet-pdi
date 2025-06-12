import math
import cv2
import numpy as np
import base64
import io

import utils.imageUtils as imgUtils


def count_repeated_values(image, pixel_value):
    height, width = image.shape
    counter = 0

    for img_line in range(height):
        for img_column in range(width):
            if image[img_line, img_column] == pixel_value:
                counter += 1

    return counter


def calculate_rk_nk_pk(image):
    rk_nk_pk = []

    height, width = image.shape
    mn = height * width

    for i in range(256):
        rk = i
        nk = count_repeated_values(image, i)
        pk = nk / mn
        rk_nk_pk.append((rk, nk, pk))

    return rk_nk_pk


def calculate_s(image):
    rk_nk_pk = calculate_rk_nk_pk(image)

    s = [0] * 256

    for i in range(256):
        s_sum = 0
        for j in range(i + 1):
            s_sum += 255 * rk_nk_pk[j][2]

        transformed_value = math.ceil(s_sum)
        s[i] = transformed_value

    return s


def equalize_histogram(image_path: str) -> str:
    original_image = imgUtils.read_image(image_path)
    image_converted_to_gray_scale = imgUtils.rgb_to_grayscale(original_image)

    s_values = calculate_s(image_converted_to_gray_scale)

    height, width = image_converted_to_gray_scale.shape

    equalized_image = np.copy(image_converted_to_gray_scale).astype(np.float32)

    for img_line in range(height):
        for img_column in range(width):
            original_pixel_value = image_converted_to_gray_scale[img_line, img_column]
            equalized_image[img_line, img_column] = s_values[original_pixel_value]

    if imgUtils.is_normalization_necessary(equalized_image):
        print('Normalização necessária!')
        equalized_image = imgUtils.normalize(equalized_image)

    equalized_image = imgUtils.convert_to_uint8(equalized_image)

    # Convert the image to base64
    _, buffer = cv2.imencode(".png", equalized_image)
    base64_image = base64.b64encode(buffer).decode("utf-8")

    return base64_image