#!/bin/python3
#
import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    result=list()
    for i in grades:
        if i<38:
            result.append(i)
            continue
        if i%5>2:
            result.append(i+(-i%5))
        else:
            result.append((i))
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
