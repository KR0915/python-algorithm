#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # n は靴下の数であり、ここでは使用されませんが、関数シグネチャに含まれています。
    # ar は靴下の配列です。

    # ar を昇順でソートします
    ar_sorted = sorted(ar)

    # ペアの数をカウントするための変数を初期化します
    pair_count = 0
    i = 0

    while i < len(ar_sorted) - 1:
        # 靴下の種類が同じ場合、ペアが成立します
        if ar_sorted[i] == ar_sorted[i + 1]:
            pair_count += 1
            # ペアを見つけたら、次のペアを探すためにインデックスを2つ進めます
            i += 2
        else:
            # 靴下の種類が異なる場合は次の要素へ進みます
            i += 1

    return pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()