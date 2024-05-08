N=int(input())
A=[]
for t in range(N):
    v=input()
    A.append(v)
Q=input()
a=[]
b=[]
for i in range(Q):
    A,B=map(int,input().split())
    for j in range(N):
        if A[j]==A:
            a.append(j)
        elif A[j]==B:
            b.append(j)
            
        
print(a)
print(b)
    
