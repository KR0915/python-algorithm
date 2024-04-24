N,Y=map(int,input().split())
flag=False
result=[]
for o10000 in range(N+1):
    for o5000 in range(N-o10000+1):
            total=o10000*10000+o5000*5000+(N-o10000-o5000)*1000
            if total==Y:
                flag=True
                a=o10000
                b=o5000
                c=N-o10000-o5000
                break
    if flag:
        break

if flag:
    print(a," ",b," ",c)
else:
    print(-1,-1,-1)