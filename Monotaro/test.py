#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    binary = bin(n)[2:]  # 2進数に変換
    result = []
    for i, bit in enumerate(binary):
        if bit == '1':
            result.append(i + 1)
            
    one_count=len(result)
    result.insert(0, one_count)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = getOneBits(n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
