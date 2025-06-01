import cv2
import numpy as np
from algorithms.highPassFilter import highPassFilter
import utils.imageUtils as imgUtils

def highBoostFilter(image_path, kernel, alpha, output_path='../outputs/bobs_reforcado.jpg'):

    image_highPass = highPassFilter(image_path, kernel)

    image_boost = alpha * image_highPass

    if imgUtils.is_normalization_necessary(image_boost):
        image_boost = imgUtils.normalize(image_boost)

    image_boost = imgUtils.convert_to_uint8(image_boost)

    cv2.imwrite(output_path, image_boost)

def main():
    image_path = '../image/bobs.jpg'
    kernel = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ], dtype=np.float32)
    alpha = 1.5
    highBoostFilter(image_path, kernel, alpha)

if __name__ == '__main__':
    main()