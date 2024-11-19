from collections import defaultdict
import heapq

Q = int(input())

# 各高さの植物の数を管理
plants = defaultdict(int)
# 現在の高さの増加量
current_growth = 0
# 植木鉢の高さを管理するためのヒープ
heights = []

# 結果を格納するリスト
results = []

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        # 高さ0の植物を1個植える（成長量を引いた高さで格納）
        adjusted_height = -current_growth
        plants[adjusted_height] += 1
        heapq.heappush(heights, adjusted_height)
    elif query[0] == '2':
        # すべての植物の高さをT増加させる
        T = int(query[1])
        current_growth += T
    elif query[0] == '3':
        # 指定された高さ以上の植物を収穫する
        H = int(query[1])
        threshold = H - current_growth
        count = 0
        # ヒープから収穫対象の植物を取り除く
        while heights and heights[0] < threshold:
            height = heapq.heappop(heights)
            count += plants[height]
            del plants[height]
        results.append(count)

# 結果の出力
for result in results:
    print(result)
