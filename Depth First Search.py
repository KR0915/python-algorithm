N = int(input())
adj = [[] for i in range(N)]
for n in range(N):
    V = list(map(int, input().split()))
    for v in V[2:]: # u,k,v1,v2,...
        adj[n].append(v-1)
d = [0] * N # 発見時刻
f = [0] * N # 完了時刻

def dfs(v, t):
    t+=1 # 発見したらインクリメント
    d[v] = t
    for next in adj[v]:
        print(next)
        if d[next] == 0: # 未発見なら
            t = dfs(next, t)
    t+=1 # 完了してもインクリメント
    f[v] = t
    return t

t = 0
for n in range(N):
    if d[n]==0: # 未発見なら
        t = dfs(n,t)
    print (n+1,d[n],f[n])