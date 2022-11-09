#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_p = 0
    count_n = 0
    count_z = 0

    for i in range(0,len(arr)):
        if arr[i] > 0:
            count_p = count_p + 1
        if arr[i] < 0:
            count_n = count_n + 1
        if arr[i] == 0:
            count_z = count_z + 1
    
    array_length = len(arr)
    # faltou o round aqui
    print(count_p/array_length)
    print(count_n/array_length)
    print(count_z/array_length)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
