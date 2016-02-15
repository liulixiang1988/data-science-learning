# -*- coding: utf-8 -*-
"""
Find the variance and standard deviation of a list of numbers

Created on Mon Feb 15 19:41:07 2016

@author: liulixiang
"""


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean


def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff


def calculate_variance(numbers):
    diff = find_differences(numbers)
    squared_diff = [d**2 for d in diff]
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))
    
    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))
