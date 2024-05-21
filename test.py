import locale
from functools import cmp_to_key
locale.setlocale(locale.LC_COLLATE, 'de_DE.UTF-8')
s=[]
total=0
ans=0
N=int(input())
for i in range(N):
    S,C=input().strip().split()
    s.append(S)
    total+=int(C)
    
sorted_s = sorted(s, key=cmp_to_key(locale.strcoll))
ans=total%N
print(sorted_s[ans])
