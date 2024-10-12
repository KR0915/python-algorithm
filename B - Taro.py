N,M=map(int,input().split())
a=[]
for _ in range(M):
    A,B=map(str,input().split())
    if A not in a and B=='M':
        a.append(A)
        print('Yes')
    else:
        print('No')