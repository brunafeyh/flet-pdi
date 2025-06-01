import cv2
import numpy as np
from algorithms.grayscale import grayscale
import utils.imageUtils as imgUtils

def meanLowPassFilter(image_path, kernel_size, output_path='../outputs/bobs_medio.jpg'):

   image = grayscale(image_path)

   height, width = np.shape(image)

   padding = kernel_size//2

   kernel = np.ones((kernel_size, kernel_size), np.float32)

   kernel /= (kernel_size*kernel_size)

   image_mean = np.zeros((height, width), np.float32)

   padded = np.pad(image, padding, mode="edge")

   for i in range(height):
       for j in range(width):
           window = padded[i:i + kernel_size, j:j + kernel_size]
           image_mean[i, j] = imgUtils.apply_correlation(window, kernel)

   if imgUtils.is_normalization_necessary(image_mean):
       image_mean = imgUtils.normalize(image_mean)

   image_mean = imgUtils.convert_to_uint8(image_mean)

   cv2.imwrite(output_path, image_mean)

def main ():
    image_path = '../image/bobs.jpg'
    kernel_size = 3
    meanLowPassFilter(image_path, kernel_size)

if __name__ == '__main__':
    main()