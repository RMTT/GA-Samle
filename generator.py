import random
import math
import time


def generate_grid(width, high, proportion):
    '''
    generate stamp grid
    :param width: width of grid
    :param high: high of grid
    :param proportion: the proportion of generate stamp,must less than 1
    :return:
    '''
    random.seed(time.time())
    if proportion > 1:
        print("proportion must less than 1")
        return None
    grid = [[[] for j in range(high)] for i in range(width)]

    A = int(proportion)
    B = 1
    while proportion - A != 0:
        B *= 10
        proportion *= 10
        A = int(proportion)

    gcd = math.gcd(A, B)
    A = int(A / gcd)
    B = int(B / gcd)

    for i in range(width):
        for j in range(high):
            if random.randint(1, B) <= A:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid


def generate_random_gene(gene, max_traits, max_genes):
    traits = [[] for i in range(max_traits)]
    for i in range(max_traits):
        traits[i] = gene[random.randint(0, max_genes - 1)]
    return traits


def generate_random_unit(number, gene, max_traits, max_genes):
    units = []
    for i in range(number):
        units.append(generate_random_gene(gene, max_traits, max_genes))
    return units


if __name__ == '__main__':
    g = generate_grid(30, 20, 0.5)
    print(g)
