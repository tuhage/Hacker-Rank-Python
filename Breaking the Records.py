#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max,min=scores[0],scores[0]
    maxCount,minCount=0,0

    for i in scores:
        if i<min:
            min=i
            minCount+=1
        if i>max:
            max=i
            maxCount+=1
    result [maxCount,minCount]



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')

    #fptr.close()
