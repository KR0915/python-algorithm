N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
L=int(input())
C=list(map(int,input().split()))
Q=int(input())
X=list(map(int,input().split()))
result=[]
ans=[]
for i in range(N):
    for j in range(M):
        for k in range(L):
            result.append(A[i]+B[j]+C[k])
          
result=set(result)
for l in range(Q):
    if X[l] in result:
        print('Yes')
    else:
        print('No')