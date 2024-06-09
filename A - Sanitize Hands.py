N,M=map(int,input().split())
H=list(map(int,input().split()))

for i in range(N):
    M-=H[i]
    if M==0:
        print(i+1)
        break
    elif M<0:
        print(i)
        break
    
if M>0:
    print(N)
    