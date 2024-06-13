N=int(input())
ans=0
head=[]
for i in range(N):
    A,B=map(int,input().split())
    ans+=A
    head.append(B-A)
    
head=max(head)

print(ans+int(head))