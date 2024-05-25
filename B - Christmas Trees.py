A,M,L,R=map(int,input().split())
l=L+(A-L)%M
r=R-(R-A)%M
print((r-l)//M+1)
    