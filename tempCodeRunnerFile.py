N=int(input())
A=list(map(int,input().split()))
result=[]
for i in range(N):
    for n in range(i):
        result.append(A[i]-A[n])
result.sort()
print(result[-1])