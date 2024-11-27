import collections

N=input()
n=collections.Counter(N)
if n['1']==1 and n['2']==2 and n['3']==3:
    print('Yes')
else:
    print('No')