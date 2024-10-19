N=int(input())
L=[]
R=[]
ans=0
for _ in range(N):
    a,s=map(str,input().split())
    if s=='L':
        L.append(a)
    else:
        R.append(a)

for i in range(len(L) - 1):
    ans += abs(int(L[i]) - int(L[i + 1]))

for i in range(len(R) - 1):
    ans += abs(int(R[i]) - int(R[i + 1]))

print(ans)