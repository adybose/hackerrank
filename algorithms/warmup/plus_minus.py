#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/plus-minus

import sys

n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
negative = 0
positive = 0
zero = 0

for num in arr:
    if num > 0: positive += 1
    if num < 0: negative += 1
    if num == 0: zero += 1

print(round(positive / n, 6))
print(round(negative / n, 6))
print(round(zero / n, 6))