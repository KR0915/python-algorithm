N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=0
A=set(A)
A=list(A)

for i in A:
    if i<=K:
        ans+=i
        
print(K*(K+1)//2-ans)