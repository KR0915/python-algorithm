#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    # Write your code here
    def dfs(person, visited):
        for other, knows in enumerate(related[person]):
            if knows == '1' and other not in visited:
                visited.add(other)
                dfs(other, visited)
    
    n = len(related)
    visited = set()
    groups = 0
    
    for person in range(n):
        if person not in visited:
            dfs(person, visited)
            groups += 1
            
    return groups

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input().strip())

    related = []

    for _ in range(related_count):
        related_item = input()
        related.append(related_item)

    result = countGroups(related)

    fptr.write(str(result) + '\n')

    fptr.close()
