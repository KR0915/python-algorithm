N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=A+B
C.sort()
flag=True
for i in range(len(C)-1):
    if C[i] in A and C[i+1] in A:
        flag=False
        print('Yes')
        break
    
if flag:
    print('No')