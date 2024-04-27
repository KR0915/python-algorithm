N=int(input())
A=list(map(int,input().split()))
count=0
result=[]
for i in range(N):
    a=A[i]
    A[a-1],A[i]=A[i],A[a-1]
    count+=1
    if a-1>i:
        result.append(i)
        result.append(a-1)
    elif a-1<i:
        result.append(a-1)
        result.append(i)
print(count)
print(result)