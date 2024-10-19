N,C=map(int,input().split())
T=list(map(int,input().split()))
count=0
count+=1
last_time=T[0]
for i in range(1,N):
    if T[i]-last_time>=C:
        count+=1
        last_time=T[i]
    
print(count)