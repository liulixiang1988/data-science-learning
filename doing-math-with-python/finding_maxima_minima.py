# -*- coding: utf-8 -*-
"""
Finding Maxima and Minma with Higher-Order Derivatives

Created on Wed Feb 24 09:12:25 2016

@author: Liu Lixiang
"""
from sympy import Symbol, solve, Derivative

x = Symbol('x')
f = x**5 - 30*x**3+50*x
d1 = Derivative(f, x).doit()
critical_points = solve(d1)
print(critical_points)
A, B, C, D = critical_points
# Second derivate
d2 = Derivative(f, x, 2).doit()
print('Second-Order Derivative:')
print(d2.subs({x:A}).evalf())
print(d2.subs({x:B}).evalf())
print(d2.subs({x:C}).evalf())
print(d2.subs({x:D}).evalf())
x_min = -5
x_max = 5
# Global Maxima
print('Global Maxima:')
print(f.subs({x:A}).evalf())
print(f.subs({x:C}).evalf())
print(f.subs({x:x_min}).evalf())
print(f.subs({x:x_max}).evalf())
# Global Minima
print('Global Minima:')
print(f.subs({x:B}).evalf())
print(f.subs({x:D}).evalf())
print(f.subs({x:x_min}).evalf())
print(f.subs({x:x_max}).evalf())
