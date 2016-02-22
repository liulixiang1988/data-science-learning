# -*- coding: utf-8 -*-
"""
Exploring Henon's Function

Created on Mon Feb 22 15:46:11 2016

@author: Liu Lixiang
"""

from matplotlib import pyplot as plt


def transformation(p):
    x, y = p
    x1 = y + 1.0 - 1.4*x**2
    y1 = 0.3*x
    return x1, y1


if __name__ == '__main__':
    n = int(input('Please input the number:'))
    p = (0, 0)
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transformation(p)
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, 'o')
    plt.title('Henon Function with {0} points'.format(n))
    plt.savefig('henon_function.png')
    plt.show()
