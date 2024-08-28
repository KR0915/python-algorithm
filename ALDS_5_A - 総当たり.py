n=int(input())
A=list(map(int,input().split()))
q=int(input())
M=list(map(int,input().split()))
total=set()
for i in range(1<<n):
    subset=[]
    subset_sum = 0
    for j in range(n):
        if (i>>j)&1:
            subset.append(A[j])
            subset_sum += A[j]
            total.add(subset_sum)
    # print(total)

for m in M:
    if m in total:
        print("yes")
    else:
        print("no")