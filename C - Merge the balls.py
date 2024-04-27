N=int(input())
A=list(map(int,input().split()))
result=[]
for i in range(N):
    M=2**int(A[i])
    result.append(M)
    print(result)
    if len(result)<=1:
        continue
    if result[-1]!=result[-2]:
        break
    elif result[-1]==result[-2]:
        new=int(result[-1])+int(result[-2])
        result.pop()
        result.pop()
        result.append(new)
        
    
    
print(len(result))