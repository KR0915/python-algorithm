N=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(N):
    B.append(A[i-1]*A[i])

del B[0]
for b in range(N-1):
    print(B[b],end=" ")