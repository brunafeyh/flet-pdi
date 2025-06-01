import matplotlib.pyplot as plt
import utils.imageUtils as imgUtils


def histogram(image_path, output_path='../outputs/output_histogram.jpg'):
    original_image = imgUtils.read_image(image_path)

    image_converted_to_gray_scale = imgUtils.rgb_to_grayscale(original_image)

    h = [0] * 256

    height, width = image_converted_to_gray_scale.shape

    for img_line in range(1, height):
        for img_column in range(1, width):
            h[ image_converted_to_gray_scale[img_line, img_column] ] += 1

    plt.figure(figsize=(10, 6))
    plt.bar(range(256), h, color='gray')
    plt.title('Histograma de Intensidade de Pixel')
    plt.xlabel('Intensidade de Pixel (0-255)')
    plt.ylabel('Número de Pixels')
    plt.xlim([-5, 260])
    plt.grid(axis='y', alpha=0.75)

    plt.savefig(output_path)
    plt.close()

def main():
    image_path = '../image/img.png'
    histogram(image_path)

if __name__ == '__main__':
    main()