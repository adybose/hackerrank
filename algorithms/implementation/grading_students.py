#!/bin/python3

# Link to the problem: https://www.hackerrank.com/challenges/grading

import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        unit = grades[i] % 10
        if grades[i] >= 38:
            if unit >= 8:
                grades[i] = (int(grades[i]/10) * 10) + 10
            elif unit >= 3 and unit <= 5:
                grades[i] = (int(grades[i]/10) * 10) + 5
                
    return grades


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
