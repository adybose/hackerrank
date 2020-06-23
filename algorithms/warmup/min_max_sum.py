#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/mini-max-sum

import sys

arr = list(map(int, input().strip().split(' ')))
total_sum = sum(x for x in arr)

min_sum = total_sum - max(arr)
max_sum = total_sum - min(arr)

print(min_sum, max_sum)