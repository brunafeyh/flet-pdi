import cv2
import numpy as np
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils

def thresholding(image_path, threshold, output_path='../outputs/bobs_limiarizado.jpg'):

    image = grayscale(image_path)

    height, width = image.shape

    binary_image = np.zeros((height, width), np.float32)

    for i in range (height):
        for j in range (width):
            if image[i, j] > threshold:
                binary_image[i, j] = 255
            else:
                binary_image[i, j] = 0

    binary_image = imgUtils.convert_to_uint8(binary_image)

    cv2.imwrite(output_path, binary_image)

def main():
    image_path = '../image/bobs.jpg'
    threshold = 127
    thresholding(image_path, threshold)

if __name__ == '__main__':
    main()