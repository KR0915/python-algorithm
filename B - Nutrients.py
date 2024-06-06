N, M = map(int, input().split())
A = list(map(int, input().split()))
X2=[0]*M
flag=True
for _ in range(N):
    X = list(map(int, input().split()))
    for i in range(M):
        X2[i]+=X[i]
        
for j in range(M):
    if A[j]>X2[j]:
        print('No')
        flag=False
        break

if flag:
    print('Yes')