M,D=map(int,input().split())
y,m,d=map(int,input().split())
ans=[]
if D==d:
    m=m+1
    d=1
    if m>M:
        m=1
        y=y+1
else:
    d=d+1
ans.append(y)
ans.append(m)
ans.append(d)
print(*ans)