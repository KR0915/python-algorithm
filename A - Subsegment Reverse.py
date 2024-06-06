N,L,R=map(int,input().split())
a=0
b=0
S=[]
S2=[]
for _ in range(N):
    a+=1
    S.append(a)
start=S[:L-1]
end=S[R:]
for i in range(L,R+1):
    S2.append(i)
S3=S2[::-1]
print(*start+S3+end,sep=" ")