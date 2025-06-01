import cv2
import numpy as np
from algorithms.meanLowPassFilter import meanLowPassFilter
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils

def medianLowPassFilter(image_path, kernel_size, output_path = '../outputs/bobs_mediano.jpg'):

    image = grayscale(image_path)

    height, width = np.shape(image)

    padding = kernel_size // 2

    image_median = np.zeros((height, width), np.float32)

    padded = np.pad(image, padding, mode="edge")

    for i in range(height):
        for j in range(width):
            window = padded[i:i + kernel_size, j:j + kernel_size]
            image_median[i, j] = np.median(window)

    if imgUtils.is_normalization_necessary(image_median):
        image_median = imgUtils.normalize(image_median)

    image_median = imgUtils.convert_to_uint8(image_median)

    cv2.imwrite(output_path, image_median)

def main():
    image_path = '../image/bobs.jpg'
    kernel_size = 3
    medianLowPassFilter(image_path, kernel_size)

if __name__ == '__main__':
    main()
