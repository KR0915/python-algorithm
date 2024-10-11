from itertools import combinations

def get_subset_sums(arr):
    subset_sums = set()
    n = len(arr)
    for i in range(n + 1):
        for comb in combinations(arr, i):
            subset_sums.add(sum(comb))
    return subset_sums

N = int(input())
K = list(map(int, input().split()))

# 部署の人数リストを2つに分ける
half = N // 2
first_half = K[:half]
second_half = K[half:]

# 各部分について全ての部分集合の和を計算
first_half_sums = get_subset_sums(first_half)
second_half_sums = get_subset_sums(second_half)

total_sum = sum(K)
min_max_group_size = float('inf')

# 2つの部分集合の和の組み合わせを試す
for s1 in first_half_sums:
    for s2 in second_half_sums:
        group_A = s1 + s2
        group_B = total_sum - group_A
        max_group_size = max(group_A, group_B)
        min_max_group_size = min(min_max_group_size, max_group_size)

print(min_max_group_size)