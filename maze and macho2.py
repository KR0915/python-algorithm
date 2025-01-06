import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid,n,m):
    visited = [[[float('inf')] * (n * m) for _ in range(m)] for _ in range(n)]

    start = None

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)

    queue = deque([(start[0], start[1], 0, 0)])
    visited[0][0][0] = 0
    times=[]

    while queue:

        x, y, broken, time = queue.popleft()

        if grid[x][y] == 'G':
            times.append(time)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '#':
                    new_broken = broken + 1
                    new_time = time + 1 + broken
                    if new_broken < n * m and visited[nx][ny][new_broken] > new_time:
                        visited[nx][ny][new_broken] = new_time
                        queue.append((nx, ny, new_broken, new_time))
                elif grid[nx][ny] == '.' or grid[nx][ny] == 'G':
                    new_time = time + 1
                    if visited[nx][ny][broken] > new_time:
                        visited[nx][ny][broken] = new_time
                        queue.append((nx, ny, broken, new_time))

    return (min(times))

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))
    n,m=map(int, lines[0].split())
    grid=[]
    for i in range(1,n+1):
        grid.append(lines[i])

    result = bfs(grid, n, m)
    print(result)
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
