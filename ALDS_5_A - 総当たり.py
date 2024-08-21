n=int(input())
A=list(map(int,input().split()))
q=int(input())
M=list(map(int,input().split()))

for i in range(1<<n):
    subset=[]
    for j in range(n):
        if (i>>j)&1:
            subset.append(A[j])
    print(subset)