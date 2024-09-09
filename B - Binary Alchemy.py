N=int(input())
matrix=[]
for i in range(N):
    A=list(map(int,input().split()))
    matrix.append(A)
    
ans = 1

for j in range(1, N + 1):
    if ans >=j:
        ans=matrix[ans-1][j-1]
    else:
        ans=matrix[j-1][ans-1]
    
    
print(ans)