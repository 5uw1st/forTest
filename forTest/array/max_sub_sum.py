#!usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:5uwst
@file:max_sub_sum.py
@time: 2019/7/22
"""

import random


def find_max_sub_sequence_sum_1(test_list):
    """
    找出最大子序列和(分治法NlogN)
    :return:
    """
    pass


def find_max_sub_sequence_sum_2(test_list):
    """
    找出最大子序列和(动态规划logN)
    :param test_list: list
    :return:
    """
    max_sum = 0
    max_temp = 0
    for i in range(len(test_list)):
        if max_temp <= 0:
            max_temp = test_list[i]
        else:
            max_temp += test_list[i]
        if max_temp > max_sum:
            max_sum = max_temp
    return max_sum


def test_sub(test_list):
    ret = find_max_sub_sequence_sum_2(test_list)
    return ret


if __name__ == '__main__':
    lst = [random.randint(-10, 10) for _ in range(10)]
    # lst = [5, 2, -3, 7, -8, 2, 3, -7, 2]
    # lst = [-2, 5, -2, 4, 3, -3, 4, -7, 8, -1, 5]
    print("List:{0}".format(lst))
    print(test_sub(test_list=lst))
