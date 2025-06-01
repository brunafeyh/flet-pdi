import cv2
import numpy as np
import utils.imageUtils as imgUtils


def roberts(image_path, output_path='../outputs/output_robert.jpg'):
    original_image = imgUtils.read_image(image_path)

    image_converted_to_gray_scale = imgUtils.rgb_to_grayscale(original_image)

    height, width = image_converted_to_gray_scale.shape

    kernel_x = np.array([
        [0,  1],
        [-1, 0]
    ], dtype=np.float32)

    kernel_y = np.array([
        [1, 0],
        [0, -1]
    ], dtype=np.float32)

    gradient_diagonal_positive = np.zeros_like(image_converted_to_gray_scale, dtype=np.float32)
    gradient_diagonal_negative = np.zeros_like(image_converted_to_gray_scale, dtype=np.float32)

    for img_line in range(height - 1):
        for img_column in range(width - 1):
            region = image_converted_to_gray_scale[img_line:img_line + 2, img_column:img_column + 2]

            gradient_diagonal_positive[img_line, img_column] = imgUtils.apply_correlation(region, kernel_x)

            gradient_diagonal_negative[img_line, img_column] = imgUtils.apply_correlation(region, kernel_y)

    magnitude = np.sqrt(gradient_diagonal_positive ** 2 + gradient_diagonal_negative ** 2)

    if imgUtils.is_normalization_necessary(magnitude):
        print('Normalização necessária!')
        magnitude = imgUtils.normalize(magnitude)

    magnitude = imgUtils.convert_to_uint8(magnitude)
    cv2.imwrite(output_path, magnitude)

def main():
    image_path = '../image/img.png'
    roberts(image_path)

if __name__ == '__main__':
    main()
