A,M,L,R=map(int,input().split())
r=((R-A)//M)*M+A
print(r)
l=((L+A)//M)*M+A
print(l)
print((r-l)//M+1)
    