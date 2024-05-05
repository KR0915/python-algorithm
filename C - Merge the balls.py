N=int(input())
A=list(map(int,input().split()))
result=[]
for i in A:
    result.append(i)
    while len(result)>=2 and result[-2]==result[-1]:
        x=result.pop()
        result.pop()
        result.append(x+1)
print(len(result))