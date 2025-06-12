import numpy as np

def parse_kernel(kernel_str: str) -> np.ndarray:
    """
    Converte a string do kernel em uma matriz quadrada numpy.
    A string deve ser uma lista de números separados por espaço, e a função irá
    calcular o tamanho da matriz (assumindo que a matriz é quadrada).
    """
    # Remove espaços extras e divide os valores
    kernel_values = list(map(int, kernel_str.strip().split()))

    # Calcula o tamanho da matriz (assumindo que é quadrada)
    n = int(len(kernel_values) ** 0.5)  # Raiz quadrada do número de elementos

    # Verifica se o número de elementos é um quadrado perfeito
    if n * n != len(kernel_values):
        raise ValueError("O número de elementos no kernel não forma uma matriz quadrada.")

    # Converte a lista em uma matriz numpy
    kernel = np.array(kernel_values).reshape((n, n))

    return kernel