N,Q=map(int,input().split())
T=list(map(int,input().split()))
count=0
t=[]
for i in range(N):
    t.append(1)
    
for i in range(Q):
    a=int(T[i])
    if t[a-1]==0:
        t[a-1]=1
    elif t[a-1]==1:
        t[a-1]=0

for i in range(N):
    if t[i]==1:
        count+=1
    
print(count)
    