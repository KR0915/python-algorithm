N,K=map(int,input().split())
A=list(map(int,input().split()))
c=0
k=K
for i in range(N):
    k-=A[i]
    if k>=0:
        continue
    else:
        k=K-A[i]
        c+=1
        
print(c+1)