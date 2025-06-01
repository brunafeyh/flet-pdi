import cv2
import numpy as np
import utils.imageUtils as imgUtils

def log(image_path, output_path='../outputs/output_log.jpg'):
    original_image = imgUtils.read_image(image_path)

    image_converted_to_gray_scale = imgUtils.rgb_to_grayscale(original_image)

    image_float = image_converted_to_gray_scale.astype(np.float32)

    c = 255 / np.log(1 + np.max(image_float))
    log_image = c * np.log(1 + image_float)

    if imgUtils.is_normalization_necessary(log_image):
        print('Normalização necessária!')
        log_image = imgUtils.normalize(log_image)

    log_image = imgUtils.convert_to_uint8(log_image)

    cv2.imwrite(output_path, log_image)

def main():
    image_path = '../image/img.png'
    log(image_path)

if __name__ == '__main__':
    main()