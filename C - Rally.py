N=int(input())
X=list(map(int,input().split()))
ans=0
result=10**18
for j in range(max(X)+1):
    ans=0
    for i in range(N):
        ans+=(X[i]-j)**2
    result=min(result,ans)
    
print(result)