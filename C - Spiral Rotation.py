N = int(input())
matrix = []
for _ in range(N):
    a = list(input().strip())
    matrix.append(a)

for row in matrix:
    print(''.join(row))

# print(matrix)
# print(matrix[0][0])

for i in range(N//2):
    for j in range(i,N+1-i):
        