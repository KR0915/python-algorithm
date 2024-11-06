N=int(input())
day=[]
ans=0
i=0
for _ in range(N):
    q,r=map(int,input().split())
    day.append((q,r))
    
Q=int(input())
for _ in range(Q):
    t,d=map(int,input().split())
    while d>ans:
        ans=int(day[t-1][0])*i+int(day[t-1][1])
        print(day[t-1][0],i,day[t-1][1])
        i+=1
    print(ans)
