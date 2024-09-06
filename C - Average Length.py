import itertools
import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def average_path_length(towns):
    n = len(towns)
    all_permutations = itertools.permutations(towns)
    total_distance = 0
    count = 0
    
    for perm in all_permutations:
        path_distance = 0
        for i in range(n - 1):
            path_distance += calculate_distance(perm[i], perm[i + 1])
        total_distance += path_distance
        count += 1
    
    return total_distance / count

# 入力を読み取る
n = int(input())
towns = []
for _ in range(n):
    x, y = map(int, input().split())
    towns.append((x, y))

# 平均経路長を計算して出力
print(average_path_length(towns))