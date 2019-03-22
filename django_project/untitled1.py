# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:23:25 2019

@author: Pinar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max=arr[0]
    for i in arr:
        if arr[i+1]> arr[i]:
            temp=arr[i+1]
            arr[i]=temp
            arr[i+1]=arr[i]
    toplam1=arr[0]+arr[1]+arr[2]+arr[3]
    toplam2=arr[4]+arr[1]+arr[2]+arr[3]
    return print (toplam1,toplam2)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
