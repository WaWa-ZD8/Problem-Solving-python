import math
import os
import random
import re
import sys


def getTotalX(a, b):
    lcm = math.lcm(*a)
    gcd = math.gcd(*b)
    count = 0
    
    for i in range(lcm, gcd + 1, lcm):
        if gcd % i == 0:
            count += 1
    
    print (count)
                
                
        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    result = getTotalX(arr, brr)
