#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records

import sys


def breakingRecords(score):
    # Complete this function
    lowest = highest = score[0]
    lc = hc = 0
    for each in score:
        if each < lowest:
            lowest = each
            lc += 1
        if each > highest:
            highest = each
            hc += 1
    return [hc, lc]


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
