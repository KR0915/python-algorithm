Q=int(input())
A=[]
for i in range(Q):
    q,k=map(int,input().split())
    if q==1:
        A.append(k)
    elif q==2:
        print(A[-k])