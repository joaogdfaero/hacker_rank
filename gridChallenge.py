#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
import string

def gridChallenge(grid):
    alphabeto = string.ascii_lowercase

    # verifica a ordem em que as letras estão em cada elemento da grid
    ordem = [[0]*len(grid)]*len(grid[0])
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            for k in range(0,len(alphabeto)):
                if grid[i][j] == alphabeto[k]:
                    print("i")
                    print(i)
                    print("j")
                    print(j)
                    print("k")
                    print(k)
                    ordem[i][j] = k
    
    print(ordem)




    











grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
gridChallenge(grid)