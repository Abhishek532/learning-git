import math
import sys

def add(a,b):
    return a + b

def divide(a,b):
    if b == 0:
        print('Denominator cannot be zero! Exiting!')
        sys.exit(-1)
    return a / b

def subtract(a,b):
    return a - b
