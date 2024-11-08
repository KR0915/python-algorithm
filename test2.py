# 入力の読み込み
N, Q = map(int, input().split())
instructions = [input().split() for _ in range(Q)]

# 初期状態
left_hand = 1
right_hand = 2
total_moves = 0

# 指示に従って手を移動
for H, T in instructions:
    T = int(T)
    if H == 'L':
        # 左手を移動
        if T != right_hand:
            distance = min(abs(left_hand - T), N - abs(left_hand - T))
            total_moves += distance
            left_hand = T
    elif H == 'R':
        # 右手を移動
        if T != left_hand:
            distance = min(abs(right_hand - T), N - abs(right_hand - T))
            total_moves += distance
            right_hand = T

# 結果の出力
print(total_moves)