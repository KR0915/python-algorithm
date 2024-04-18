# マス目の状態を入力として受け取る
s1, s2, s3 = map(int, input().split())

# ビー玉が置かれるマスの数を数える
count = 0
if s1 == 1:
    count += 1
if s2 == 1:
    count += 1
if s3 == 1:
    count += 1

# 結果を出力
print(count)
