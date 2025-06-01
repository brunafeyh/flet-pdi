import cv2
import numpy as np

def rgb_to_grayscale(image):
    print('INFO - Realizando conversão para escala de cinza.')
    height, width, channels = image.shape

    image_converted_to_gray_scale = np.zeros((height, width), dtype=np.uint8)

    for img_line in range(height):
        for img_column in range(width):
            red_pixel_value, green_pixel_value, blue_pixel_value = image[img_line, img_column]

            image_converted_to_gray_scale[img_line, img_column] = int(
                0.299 * red_pixel_value +
                0.587 * green_pixel_value +
                0.114 * blue_pixel_value
            )

    return image_converted_to_gray_scale

def read_image(image_path):
    print('INFO - Realizando leitura da imagem.')
    return cv2.imread(image_path)


def apply_correlation(region, kernel):
    result = 0

    for line in range(kernel.shape[0]):
        for column in range(kernel.shape[1]):
            result += region[line, column] * kernel[line, column]

    return result

def calculate_magnitude(gradient_x, gradient_y):
    print('INFO - Calculando magnitude da imagem.')

    height, width = gradient_x.shape

    magnitude = np.zeros_like(gradient_x, dtype=np.float32)

    for line in range(height):
        for column in range(width):
            g_x_squared = gradient_x[line, column] ** 2
            g_y_squared = gradient_y[line, column] ** 2

            magnitude[line, column] = np.sqrt(g_x_squared + g_y_squared)

    return magnitude

def normalize(image):
    print('INFO - Realizando normalização na imagem.')
    min_pixel_value = np.min(image)
    max_pixel_value = np.max(image)

    normalized = (image - min_pixel_value) / (max_pixel_value - min_pixel_value) * 255.0
    return normalized

def convert_to_uint8(image):
    print('INFO - Realizando conversão da imagem para uint8.')
    return image.astype(np.uint8)

def is_normalization_necessary(image):
    print('INFO - Realizando verificação se é necessário normalizar a imagem.')
    min_pixel_value = np.min(image)
    max_pixel_value = np.max(image)

    return min_pixel_value < 0 or max_pixel_value > 255

def have_same_size(image1, image2):
    shape1 = image1.shape
    shape2 = image2.shape

    return shape1[:2] == shape2[:2]

def is_grayscale(image_path):
    image = cv2.imread(image_path)
    if len(image.shape) == 2:
        print('INFO - A imagem esta em escala de cinza.')
        return True