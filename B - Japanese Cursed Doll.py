N,T,P=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
L=L[-P:]
if L[0]>T:
    print(0)
else:
    print(T-L[0])
