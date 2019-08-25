#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    v={'U':1,'D':-1}
    t=0
    T=[0]
    c=0
    for i in s:
        t+=v[i]
        if T[-1]<0 and t==0:
            c+=1
        T.append(t)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

