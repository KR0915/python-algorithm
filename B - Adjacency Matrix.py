N=int(input())
matrix=[]
for i in range(N):
    matrix_temp=[int(x)for x in input().split(" ")]
    matrix.append(matrix_temp)
for a in range(N):
    result=[]
    for b in range(N):
        if matrix[a][b]==1:
            result.append(b+1)
    if result:
        print(*result)
    