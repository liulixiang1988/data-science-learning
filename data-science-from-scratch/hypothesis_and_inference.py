# -*- coding:utf-8 -*-
from probability import normal_cdf, inverse_normal_cdf
import math
import random


def normal_approximation_to_binomial(n, p):
    """使用正态分布拟合伯努利实验"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# 一个变量低于阈值以下的概率
normal_probability_below = normal_cdf


def normal_probability_above(lo, mu=0, sigma=1):
    """阈值高于某个值以下的概率"""
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu=0, sigma=1):
    """阈值在两个值之间的概率"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    """阈值在两个值之外的概率"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)
