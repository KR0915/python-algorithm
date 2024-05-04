N,S,K=map(int,input().split())
result=0
for i in range(N):
    A,B=map(int,input().split())
    result+=A*B
if result<S:
    print(result+K)
elif result>=S:
    print(result)
    
