# -*- coding:utf-8 -*-
import math
from functools import reduce

#
# 向量的函数
#


def vector_add(v, w):
    """向量加法"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """向量减法"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """多个向量的加法"""
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """数字与向量相乘"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """计算向量的均值"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    """向量的点乘"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """向量的平方"""
    return dot(v, v)


def magnitude(v):
    """向量的大小(长度)"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """"两个向量距离的平法"""
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    """向量之间的距离"""
    return math.sqrt(squared_distance(v, w))

#
# 矩阵的函数
#


def shape(A):
    """矩阵的形状"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    """获取行"""
    return A[i]


def get_column(A, j):
    """获取列"""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """使用entry_fn这个函数来创建矩阵"""
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    """单元矩阵生成函数"""
    return 1 if i == j else 0

identity_matix = make_matrix(5, 5, is_diagonal)


#          user 0  1  2  3  4  5  6  7  8  9
#
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

#####
# DELETE DOWN
#


def matrix_add(A, B):
    """矩阵相加"""
    if shape(A) != shape(B):
        raise ArithmeticError("cannot add matrices with different shapes")

    num_rows, num_cols = shape(A)

    def entry_fn(i, j):
        return A[i][j] + B[i][j]

    return make_matrix(num_rows, num_cols, entry_fn)


def make_graph_dot_product_as_vector_projection():
    from matplotlib import pyplot as plt
    v = [2, 1]
    w = [math.sqrt(.25), math.sqrt(.75)]
    c = dot(v, w)
    vonw = scalar_multiply(c, w)
    o = [0, 0]

    plt.arrow(0, 0, v[0], v[1],
              width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("v", v, xytext=[v[0] + 0.1, v[1]])
    plt.arrow(0, 0, w[0], w[1],
              width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("w", w, xytext=[w[0] - 0.1, w[1]])
    plt.arrow(0, 0, vonw[0], vonw[1], length_includes_head=True)
    plt.annotate(u"(v•w)w", vonw, xytext=[vonw[0] - 0.1, vonw[1] + 0.1])
    plt.arrow(v[0], v[1], vonw[0] - v[0], vonw[1] - v[1],
              linestyle='dotted', length_includes_head=True)
    plt.scatter(*zip(v, w, o), marker='.')
    plt.axis('equal')
    plt.show()
