#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    i = 1
    if len(s) == 1:
        return s

    while i < len(s):
        if s[i] == s[i-1]:
            if len(s) == 2:
                return 'Empty String'
            s = s[:i-1]+s[i+1:]
            i = 1
        else:
            i += 1

    if len(s) == 0:
        return 'Empty String'


    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

