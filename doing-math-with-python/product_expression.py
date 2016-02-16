# -*- coding: utf-8 -*-
"""
Product of two expressions

Created on Tue Feb 16 14:38:14 2016

@author: Liu Lixiang
"""

from sympy import expand, sympify, pprint
from sympy.core.sympify import SympifyError


def product(expr1, expr2):
    prod = expand(expr1*expr2)
    pprint(prod)

if __name__=='__main__':
    expr1 = input('Enter the first expression:')
    expr2 = input('Enter the second expression:')
    
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid Input')
    else:
        product(expr1, expr2)
