import random
import math


def print_matrix(matrix):
    print('\n')
    for i in range(len(matrix)):
        print(matrix[i])


def create_directed_matrix(seed, length, k):
    random.seed(seed)
    matrix = [[random.uniform(0, 2) for _ in range(length)] for _ in range(length)]
    direct_matrix = [[math.floor(matrix[i][j] * k) for j in range(length)] for i in range(length)]
    return direct_matrix





