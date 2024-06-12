N,T=map(int,input().split())
A=list(map(int,input().split()))
tate=[0]*N
yoko=[0]*N
naname1=0
naname2=0
ans=-1

for i in range(T):
    t,y=(A[i]-1)//N,(A[i]-1)%N
    tate[t]+=1
    yoko[y]+=1
    if t==y:
        naname1+=1
    if t+y==N-1:
        naname2+=1
    if tate[t]==N or yoko[y]==N or naname1==N or naname2==N:
        ans=i+1
        break

print(ans)