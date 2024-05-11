N,X=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for i in range(N):
    if X>=A[i]:
        ans+=A[i]
print(ans)