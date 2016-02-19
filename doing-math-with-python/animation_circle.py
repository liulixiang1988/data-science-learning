# -*- coding: utf-8 -*-
"""
A growing circle

Created on Fri Feb 19 15:32:13 2016

@author: Liu Lixiang
"""

from matplotlib import pyplot as plt
from matplotlib import animation


def create_circle():
    return plt.Circle((0, 0), 0.05)


def update_radius(i, circle):
    circle.radius = i*0.5
    return circle


def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_radius, fargs=(circle,),
                                   frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()

if __name__ == '__main__':
    create_animation()
