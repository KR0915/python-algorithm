N=int(input())
A=list(map(int,input().split()))
count=0
for i in range(N):
    if A[i]==i+1:
        count+=1
        if A[i]==(i+1)*10+i+1:
            count+=1
    elif A[i]==(i+1)*10+i+1:
        count+=1
print(count)