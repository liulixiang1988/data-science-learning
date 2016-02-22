# -*- coding: utf-8 -*-
"""
Exploring Henon's Function Animation

Created on Mon Feb 22 16:09:41 2016

@author: Liu Lixiang
"""

from matplotlib import pyplot as plt
from matplotlib import animation


def transformation(p):
    x, y = p
    x1 = y + 1.0 - 1.4*x**2
    y1 = 0.3*x
    return x1, y1


def update_points(i, x, y, plot):
    plot.set_data(x[:i], y[:i])
    return plot,


if __name__ == '__main__':
    n = int(input('Please input the number:'))
    p = (0, 0)
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transformation(p)
        x.append(p[0])
        y.append(p[1])
    fig = plt.gcf()
    ax = plt.axes(xlim=(min(x), max(x)),
                  ylim=(min(y), max(y)))
    plot = plt.plot([], [], 'o')[0]
    anim = animation.FuncAnimation(fig, update_points,
                                   fargs=(x, y, plot),
                                   frames=len(x), interval=25)
    plt.title('Henon Function Animation with {0} points'.format(n))
    plt.show()
