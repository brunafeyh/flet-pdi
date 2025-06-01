import cv2

import utils.imageUtils as imgUtils


def sum(image_path1, image_path2, output_path='../outputs/output_sum.jpg'):
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    result = image_converted_to_gray_scale1 + image_converted_to_gray_scale2

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)
    cv2.imwrite(output_path, result)

def sub(image_path1, image_path2, output_path='../outputs/output_sub.jpg'):
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    result = image_converted_to_gray_scale1 - image_converted_to_gray_scale2

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)
    cv2.imwrite(output_path, result)

def mul(image_path1, image_path2, output_path='../outputs/output_mul.jpg'):
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    result = image_converted_to_gray_scale1 * image_converted_to_gray_scale2

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)
    cv2.imwrite(output_path, result)

def div(image_path1, image_path2, output_path='../outputs/output_div.jpg'):
    original_image1 = imgUtils.read_image(image_path1)
    original_image2 = imgUtils.read_image(image_path2)

    if not imgUtils.have_same_size(original_image1, original_image2):
        print('Imagens não possuem o mesmo tamanho!')
        return

    image_converted_to_gray_scale1 = imgUtils.rgb_to_grayscale(original_image1)
    image_converted_to_gray_scale2 = imgUtils.rgb_to_grayscale(original_image2)

    epsilon = 1e-5
    safe_divisor = image_converted_to_gray_scale2 + epsilon

    result = image_converted_to_gray_scale1 / safe_divisor

    if imgUtils.is_normalization_necessary(result):
        print('Normalização necessária!')
        result = imgUtils.normalize(result)

    result = imgUtils.convert_to_uint8(result)
    cv2.imwrite(output_path, result)

def main():
    image_path1 = '../image/img.png'
    image_path2 = '../image/img.png'
    sum(image_path1, image_path2)
    sub(image_path1, image_path2)
    mul(image_path1, image_path2)
    div(image_path1, image_path2)

if __name__ == '__main__':
    main()