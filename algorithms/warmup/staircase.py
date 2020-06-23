#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/staircase

import sys

n = int(input().strip())

for i in range(n):
    for j in range(n-i-1):
        print(' ', end = '')
    for k in range(i+1):
        print('#', end = '')
    print()
