#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a_list = list(range(1, 100)) #possiveis numeros de 1 a 100
    contador = [0]*len(a_list) #contador de quanto cada numero aparece

    for i in range(0,len(a)):
        for j in range(0,len(a_list)):
            if a[i] == a_list[j]:
                contador[j] = contador[j]+1
    
    for i in range(0,len(contador)):
        if contador[i] == 1:
            print(i+1)
            return i+1



    



#a = list(map(int, input().rstrip().split()))
a = [1,2,3,4,3,2,1]
lonelyinteger(a)
