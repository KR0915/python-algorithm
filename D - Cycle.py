from collections import deque
N,M=map(int,input().split())
g=[list()for _ in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

inf=10**9
d=[inf]*N
Q=deque()
d[0]=0
Q.append(0)

while Q:
    v=Q.popleft()
    for i in g[v]:
        if i==0:
            print(d[v]+1)
            exit()
        if d[i]==inf:
            d[i]=d[v]+1
            Q.append(i)
print(-1)
