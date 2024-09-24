N=int(input())
H=list(map(int,input().split()))

ans=0
for j in range(N):
    ans+=(H[j]//5)*3+(H[j]%5)*1
    
print(ans)