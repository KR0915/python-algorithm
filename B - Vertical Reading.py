# 入力を受け取る
S, T = input().split()

# 文字列の長さを取得
max_len = max(len(S), len(T))

# 縦読み用のリストを作成
vertical_reading = []

# 縦に読み取る
for i in range(max_len):
    if i < len(S):
        vertical_reading.append(S[i])
    if i < len(T):
        vertical_reading.append(T[i])

# 結果を出力
print("".join(vertical_reading))