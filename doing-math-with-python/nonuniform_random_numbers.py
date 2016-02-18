# -*- coding: utf-8 -*-
"""
Simulate a fictional ATM that dispenses dollar bills
of various denominations with varying probability

Created on Thu Feb 18 10:21:34 2016

@author: Liu Lixiang
"""

import random


def get_index(probability):
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    r = random.random()
    #print(sum_probability, r)
    for index, sp in enumerate(sum_probability):
        if r <= sp:
            return index
    return len(probability) - 1


def dispense():
    dollar_bills = [5, 10, 20, 50]
    probability = [1/6, 1/6, 1/3, 1/3]
    bill_index = get_index(probability)
    return dollar_bills[bill_index]

if __name__ == '__main__':
    s = (dispense() for i in range(1000))
    from collections import Counter
    c = Counter(s)
    print(c.most_common()) 
