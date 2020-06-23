#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/birthday-cake-candles

import sys


def birthday_cake_candles(n, ar):
    max_candle_height = max(ar)
    c = 0
    for candle_height in ar:
        if candle_height ==  max_candle_height:
            c += 1
    return c


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthday_cake_candles(n, ar)
print(result)
