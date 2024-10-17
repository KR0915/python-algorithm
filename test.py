from collections import deque

def bfs(n, m, grid, start, goal):
    # 移動方向 (上下左右)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 幅優先探索 (BFS) の初期化
    queue = deque([(start[0], start[1], 0, 0)])  # (x, y, 壊した壁の数, コスト)
    max_walls = n * m
    visited = [[[False] * (max_walls + 1) for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]][0] = True
    
    while queue:
        x, y, broken_walls, cost = queue.popleft()
        
        # ゴールに到達した場合
        if (x, y) == goal:
            return cost
        
        # 隣接するセルに移動
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '#' and broken_walls + 1 <= max_walls and not visited[nx][ny][broken_walls + 1]:
                    # 壁を壊して移動
                    queue.append((nx, ny, broken_walls + 1, cost + 1 + broken_walls))
                    visited[nx][ny][broken_walls + 1] = True
                elif grid[nx][ny] == '.' and not visited[nx][ny][broken_walls]:
                    # 床を移動
                    queue.append((nx, ny, broken_walls, cost + 1))
                    visited[nx][ny][broken_walls] = True
    
    # ゴールに到達できなかった場合
    return -1

def main():
    # 入力の読み込み
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    
    # スタートとゴールの位置を見つける
    start = None
    goal = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
    
    # 幅優先探索 (BFS) を実行して最短経路を見つける
    result = bfs(n, m, grid, start, goal)
    
    # 結果の出力
    if result != -1:
        print(result)
    else:
        print("Goal not reachable")

if __name__ == '__main__':
    main()