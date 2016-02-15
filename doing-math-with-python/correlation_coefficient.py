# -*- coding: utf-8 -*-
"""
Calculating the Correlation Coefficient

Created on Mon Feb 15 20:22:58 2016

@author: liulixiang
"""


def find_corr_x_y(x, y):
    n = len(x)

    prod = (xi*yi for xi, yi in zip(x, y))
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = (xi**2 for xi in x)
    x_square_sum = sum(x_square)

    y_square = (yi**2 for yi in y)
    y_square_sum = sum(y_square)

    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_item1 = n*x_square_sum - squared_sum_x
    denominator_item2 = n*y_square_sum - squared_sum_y
    denominator = denominator_item1 * denominator_item2
    correlation = numerator / denominator
    return correlation
