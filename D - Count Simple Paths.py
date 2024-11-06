H, W, K = map(int, input().split())
matrix = []
for _ in range(H):
    matrix.append(list(input()))

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def is_valid(x, y):
    return 0 <= x < H and 0 <= y < W and matrix[x][y] == '.'

def dfs(x, y, depth):
    if depth == K:
        return 1
    count = 0
    matrix[x][y] = '#'
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            count += dfs(nx, ny, depth + 1)
    matrix[x][y] = '.'
    return count

total_paths = 0
for i in range(H):
    for j in range(W):
        if matrix[i][j] == '.':
            total_paths += dfs(i, j, 0)

print(total_paths)