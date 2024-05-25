A,B=map(int,input().split())
ans={1,2,3}
ans.discard(A)
ans.discard(B)
if len(ans)==1:
    print(ans.pop())
else:
    print(-1)