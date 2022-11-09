#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    menor = min(arr) #menor valor
    maior = max(arr) #maior valor

    # menor soma não tenho o maior valor
    menor_soma = sum(arr) - maior
    
    #
    maior_soma = sum(arr) - menor

    print(menor_soma, maior_soma)
    

if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    arr = [1,2,3,4,5]


    miniMaxSum(arr)
