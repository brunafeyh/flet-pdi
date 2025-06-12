import cv2
import numpy as np
from algorithms.highPassFilter import highPassFilter
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils

def highBoostFilter(image_path, kernel, alpha, output_path='../outputs/output_highBoost.jpg'):
    image = grayscale(image_path)

    image_highPass = highPassFilter(image_path, kernel)

    image_boost = alpha * image_highPass + image

    if imgUtils.is_normalization_necessary(image_boost):
        image_boost = imgUtils.normalize(image_boost)

    image_boost = imgUtils.convert_to_uint8(image_boost)

    cv2.imwrite(output_path, image_boost)

def main():
    image_path = '../image/bobs.jpg'
    kernel = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ], dtype=np.float32)
    alpha = 1.5
    highBoostFilter(image_path, kernel, alpha)

if __name__ == '__main__':
    main()