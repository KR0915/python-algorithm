from collections import Counter
N=int(input())
S = input().split()
s=Counter(S)
counter=0
for i,j in s.items():
    counter+=j//2
print(counter)