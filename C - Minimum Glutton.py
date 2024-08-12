N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
sum_A=0
sum_B=0
flag=True
for i in range(1,N+1):
    sum_A+=A[-i]
    sum_B+=B[-i]
    if sum_A>X or sum_B>Y:
        print(i)
        flag=False
        break
    
if flag:
    print(N)