# -*- coding: utf-8 -*-
"""
Example of drawing a horizontal bar chart

Created on Sun Feb 14 22:23:09 2016

@author: liulixiang
"""

import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    # Number of bars
    num_bars = len(data)
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    plt.grid()
    plt.savefig('horizontal_bar.png')
    plt.show()

if __name__ == '__main__':
    steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps, labels)
