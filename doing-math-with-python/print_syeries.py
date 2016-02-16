# -*- coding: utf-8 -*-
"""
Print a Serires

Created on Tue Feb 16 13:30:27 2016

@author: Liu Lixiang
"""

from sympy import Symbol, pprint, init_printing


def print_series(n):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

if __name__=='__main__':
    n = input('Enter the number of terms you want in the series:')
    print_series(int(n))
