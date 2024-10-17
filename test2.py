from collections import deque

# 方向ベクトル (上、下、左、右)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid, n, m):
    # 各状態を保存するための配列
    # visited[x][y][w] は座標 (x, y) に w 回壁を壊して到達したときの時間を表す
    visited = [[[float('inf')] * (n * m) for _ in range(m)] for _ in range(n)]
    
    start = None
 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
    
    # キューの初期化 (スタート位置は (0, 0), 壊した壁の数 0, 時間 0)
    queue = deque([(start[0], start[1], 0, 0)])  # (x, y, 壊した壁の数, 時間)
    visited[0][0][0] = 0

    while queue:
        x, y, broken, time = queue.popleft()

        # ゴールに到達したらその時点の時間を返す
        if grid[x][y] == 'G':
            return time

        # 4方向に移動する
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # グリッド範囲内か確認
            if 0 <= nx < n and 0 <= ny < m:
                # 壁を壊す必要がある場合
                if grid[nx][ny] == '#':
                    new_broken = broken + 1
                    new_time = time + 1 + broken  # 壊すのに壊した回数分の追加時間がかかる
                    if new_broken < n * m and visited[nx][ny][new_broken] > new_time:
                        visited[nx][ny][new_broken] = new_time
                        queue.append((nx, ny, new_broken, new_time))
                # 壁でない場合は通常の移動
                elif grid[nx][ny] == '.' or grid[nx][ny] == 'G':
                    new_time = time + 1
                    if visited[nx][ny][broken] > new_time:
                        visited[nx][ny][broken] = new_time
                        queue.append((nx, ny, broken, new_time))
                        
        print(queue)

    # ゴールにたどり着けない場合
    return -1

# 入力
# n, m = 3, 3
# grid = [
#     ['S', '#', '#'],
#     ['#', '#', '.'],
#     ['#', '.', 'G']
# ]

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input())
    



# ゴリラくんがゴールに到達するのにかかる最小時間を求める
result = bfs(grid, n, m)
print(result)
