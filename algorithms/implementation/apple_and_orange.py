#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/apple-and-orange

import sys


def appleAndOrange(s, t, a, b, apple, orange):
    # Complete this function
    apple_count = 0
    orange_count = 0
    for app in apple:
        if(app+a >= s and app+a <= t):
            apple_count += 1

    for orn in orange:
        if(orn+b <= t and orn+b >= s):
            orange_count += 1

    return [apple_count, orange_count]


if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))
