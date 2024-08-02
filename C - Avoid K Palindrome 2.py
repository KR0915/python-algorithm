import itertools
N,K=map(int,input().split())
S=input()
s=set(itertools.permutations(S))
result=[''.join(i) for i in s]
print(result)
flag=False
for j in s:
    for i in range(N-1):
        if s[i]==s[i+1]:
            break
