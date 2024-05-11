N=int(input())
H=list(map(int,input().split()))
ans=0
for i in range(1,N+1):
    if H[0]<H[-i]:
        ans=N-i+1
if ans==0:
    print(-1)
else:
    print(ans)