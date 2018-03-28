#!/bin/python3

# Link to the problem: https://www.hackerrank.com/challenges/a-very-big-sum

import sys

def a_very_big_sum(n, arr):
    sum = 0
    for x in arr:
        sum += x
    
    return sum
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = a_very_big_sum(n, ar)
print(result)

