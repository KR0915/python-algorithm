N,T=map(int,input().split())
A=list(map(lambda x:int(x),input().split()))

row=[0]*N
col=[0]*N
diag=[0]*2

for i in range(T):
    x=A[i]//N
    y=A[i]%N
    
    row[x]+=1
    print(row[x])
    if row[x]==N:
        print(i+1)
        exit()