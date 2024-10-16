from collections import deque

# 入力の読み込み
n, m = map(int, input().split())
s = []
wall=0
for _ in range(n):
    S = input()
    s.append(S)

# スタートとゴールの位置を見つける
start = None
goal = None
for i in range(n):
    for j in range(m):
        if s[i][j] == 'S':
            start = (i, j)
        elif s[i][j] == 'G':
            goal = (i, j)

# スタートとゴールの位置を確認
print("Start:", start)
print("Goal:", goal)

# 幅優先探索 (BFS) の初期化
queue = deque([(start[0], start[1], 0)])  # (x, y, cost)
visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True

# 移動方向 (上下左右)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS の実行
while queue:
    x, y, cost = queue.popleft()
    
    # 現在の位置とコストを確認
    print("Current position:", (x, y), "Cost:", cost)
    
    # ゴールに到達した場合
    if (x, y) == goal:
        print("Reached goal with cost:", cost)
        break
    
    # 隣接するセルに移動
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if s[nx][ny] == '#':
                queue.append((nx, ny, cost + 1+wall))  # 壁を壊すのに1分かかる
                wall+=1
            elif s[nx][ny] == '.':
                queue.append((nx, ny, cost + 1))  # 床を移動するのに1分かかる
            visited[nx][ny] = True

# ゴールに到達できなかった場合
else:
    print("Goal not reachable")