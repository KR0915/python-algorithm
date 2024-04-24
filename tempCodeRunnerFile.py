N,Y=map(int,input().split())
flag=False
result=[]
for o10000 in range(N+1):
    for o5000 in range(N+1):
        o1000=N-o10000-o5000
        total=o10000*10000+o5000*5000+o1000*1000
        if total==Y and o10000+o5000+o1000==N:
            flag=True
            a=o10000
            b=o5000
            c=o1000
            break
    if flag:
        break

if flag:
    print(a," ",b," ",c)
else:
    print(-1,-1,-1)