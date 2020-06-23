#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/between-two-sets

import sys


def getTotalX(a, b):
    c = 0
    for i in range(max(a), min(b) + 1):
        if all(i % each == 0 for each in a) and all(each % i == 0 for each in b):
            c += 1

    return c


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
