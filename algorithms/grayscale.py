import cv2
import numpy as np
import utils.imageUtils as imgUtils

def grayscale(image_path, output_path='../outputs/bobs_cinzado.jpg'):
    image = imgUtils.read_image(image_path)
    height, width = image.shape[:2]
    image_gray = np.zeros((height, width), np.float32)

    for i in range (height):
        for j in range (width):
            B, G, R = image[i, j]
            image_gray[i, j] = int(0.114*B + 0.587*G + 0.299*R)

    image_gray = imgUtils.convert_to_uint8(image_gray)

    cv2.imwrite(output_path, image_gray)

    return image_gray

def main():
    image_path = '../image/bobs.jpg'
    grayscale(image_path)

if __name__ == '__main__':
    main()