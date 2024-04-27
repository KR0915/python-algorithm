N=int(input())
A=list(map(int,input().split()))
result=[]
for i in range(N):
    M=2**int(A[i])
    result.append(M)
    
    if len(result) > 1 and result[-1] == result[-2]:
        while len(result) > 1 and result[-1] == result[-2]:
            new = result[-1] + result[-2]
            result.pop()
            result.pop()
            result.append(new)
    elif result[-1]!=result[-2]:
        break
    
    
print(len(result))