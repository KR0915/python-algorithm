import math
N=int(input())
tmp=[0,0]
ans=0
for _ in range(N):
    X,Y=map(int,input().split())
    ans += math.sqrt((tmp[0] - X)**2 + (tmp[1] - Y)**2)
    tmp[0]=X
    tmp[1]=Y
    
ans += math.sqrt((tmp[0] - 0)**2 + (tmp[1] - 0)**2)
print(ans)
    