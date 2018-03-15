#!/bin/python3

# Link to the problem: https://www.hackerrank.com/challenges/simple-array-sum

import sys

def simple_array_sum(n, ar):
    s = 0
    for i in range(len(ar)):
        s += ar[i]
    return s


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = simpleArraySum(n, ar)
    print(result)