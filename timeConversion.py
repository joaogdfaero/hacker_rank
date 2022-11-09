#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[len(s)-2:len(s)] == "PM" and float(s[0:2]) < 12:
        # remove PM
        s = s[0:len(s)-1]
        # soma 12
        novo_horario = int(s[0:2]) + 12
        s = s[2:-1] # deleta o antigo
        # coloca o novo horario
        return str(novo_horario)+s
        
    # falta o caso em que é meia noite
    
    # falta o caso em que é meio dia
    
    # falta o caso em que é de manhã




s = "07:05:45PM"
timeConversion(s)

