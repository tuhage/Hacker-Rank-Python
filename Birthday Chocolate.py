#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    loopnumber=len(s)-m+1
    k=0
    sum=0
    result=0
    for i in range(loopnumber):
        for j in s[k:k+m]:
            sum+=j
        k+=1
        if sum==d:
            result+=1
        sum=0
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

    #fptr.close()
