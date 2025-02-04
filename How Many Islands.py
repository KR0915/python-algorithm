import sys
sys.setrecursionlimit(10**7) #再帰回数の上限変更

# マスy,xに隣接する陸を海に置き換え
#自分のマスの上下左右斜めの９マスを見る
def dfs(y,x):
    # 現在地を0に置き換え
    field[y][x] = 0
    # 周囲8マスをループ
    for dx in range(-1,2):
        for dy in range(-1,2):
            # 移動後のマスをny,nxとする
            ny = y + dy
            nx = x + dx

            # ny,nxがfield内で陸かどうかを判別
            if 0 <= nx < w and 0 <= ny < h and field[ny][nx] == 1:
                dfs(ny,nx)
    return


while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    field = []
    for _ in range(h):
        array = list(map(int,input().split()))
        field.append(array)
    
    # 島の数
    ans = 0

    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i,j)
                ans += 1

    print(ans)