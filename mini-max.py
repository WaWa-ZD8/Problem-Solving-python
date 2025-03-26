import math
import os
import random
import re
import sys

# def miniMaxSum(arr):
#     total2 = 0
#     total_list = []
    
#     total = sum(arr)
#     for i in range(len(arr)):
#         total2 = total-arr[i]
#         total_list.append(total2) 
#     min_and_max = [min(total_list), max(total_list)]    
#     print(" ".join(map(str, min_and_max)))

    
# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)
def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
