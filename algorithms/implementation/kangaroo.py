#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/kangaroo

import sys


def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'NO'  # since x1 < x2
    else:
        j = (x1 - x2) // (v2 - v1)  #
    if j > 0 and (x1 + (v1 * j) == x2 + (v2 * j)):
        return 'YES'
    else:
        return 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
