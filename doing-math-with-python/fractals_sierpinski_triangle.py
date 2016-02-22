# -*- coding: utf-8 -*-
"""
Fractals: Sierpinski Triangle

Created on Mon Feb 22 15:26:18 2016

@author: Liu Lixiang
"""

from matplotlib import pyplot as plt
import random


def transformation_1(p):
    x, y = 0.5*p[0], 0.5*p[1]
    return x, y


def transformation_2(p):
    x, y = 0.5*p[0]+0.5, 0.5*p[1]+0.5
    return x, y


def transformation_3(p):
    x, y = 0.5*p[0]+1, 0.5*p[1]
    return x, y


def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability) - 1


def transform(p):
    transformations = [transformation_1, transformation_2, transformation_3]
    probability = [1/3, 1/3, 1/3]
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p)
    return x, y


def draw_triangle(n):
    x, y = [0], [0]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y


if __name__ == '__main__':
    n = int(input('Please input the number:'))
    x, y = draw_triangle(n)
    plt.plot(x, y, 'o')
    plt.title('The triangle with {0} points'.format(n))
    plt.savefig('fractals_sierpinski_triangle.png')
    plt.show()
