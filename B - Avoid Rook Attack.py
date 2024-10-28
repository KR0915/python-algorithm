matrix=[]
for _ in range(8):
    matrix.append(list(input()))
    
check=[]
count=0
for i in range(8):
    for j in range(8):
        if matrix[i][j]=='#':
            check.append((i,j))
            
for i, j in check:
    for col in range(8):
        matrix[i][col] = '#'
    for row in range(8):
        matrix[row][j] = '#'
        
for i in range(8):
    for j in range(8):
        if matrix[i][j]=='.':
            count+=1
            
print(count)