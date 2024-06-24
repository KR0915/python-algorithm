N=int(input())
A=list(map(int,input().split()))
c=0
for i in range(2*N-2):
    if A[i]==A[i+2]:
        c+=1

print(c)