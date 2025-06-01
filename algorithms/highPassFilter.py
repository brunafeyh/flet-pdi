import cv2
import numpy as np
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils

def highPassFilter(image_path, kernel, output_path='../outputs/bobs_passaltado.jpg'):

    image = grayscale(image_path)

    height, width = image.shape

    kernel_size = kernel.shape[0]

    padding = kernel_size//2

    padded = np.pad(image, padding, mode='edge')

    image_highPass = np.zeros((height, width), np.float32)

    for i in range(height):
        for j in range(width):
            window = padded[i:i+kernel_size, j:j+kernel_size]
            image_highPass[i, j] = imgUtils.apply_correlation(window, kernel)

    if imgUtils.is_normalization_necessary(image_highPass):
        image_highPass = imgUtils.normalize(image_highPass)

    image_highPass = imgUtils.convert_to_uint8(image_highPass)

    cv2.imwrite(output_path, image_highPass)

    return image_highPass

def main():
    image_path = '../image/bobs.jpg'
    kernel = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ], dtype=np.float32)
    highPassFilter(image_path, kernel)

if __name__ == '__main__':
    main()