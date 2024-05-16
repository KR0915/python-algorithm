N=int(input())
A=list(map(int,input().split()))
c=1
for i in range(N-1):
    if A[i]==A[i+1]:
        c+=1
    else:
        break
if c==N:
    print('Yes')
else:
    print('No')
