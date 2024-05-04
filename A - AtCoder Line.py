N,X,Y,Z=map(int,input().split())
p=X
flag=False
for i in range(N):
    X+=1
    p-=1
    if X==Z:
        flag=True
        break
    if p==Z:
        flag=True
        break
    if X==Y or p==Y:
        break
    
    
if flag:
    print("Yes")
else:
    print("No")
