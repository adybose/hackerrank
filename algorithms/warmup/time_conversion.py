#!/bin/python3
# Link to the problem: https://www.hackerrank.com/challenges/time-conversion

import sys


def time_conversion(s):
    s = list(s.split(':'))
    hh, mm, ss = s
    hh = int(hh)
    if ss[-2] == 'P':
        if hh < 12:
            hh += 12
    elif ss[-2] == 'A':
        if hh == 12:
            hh = 0
    hh = str('{0:02d}'.format(hh))
    ss = ss[:2]
    s = [hh, mm, ss]
    return s


s = input().strip()
result = time_conversion(s)
print(':'.join(str(x) for x in result))
