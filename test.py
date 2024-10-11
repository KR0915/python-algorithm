def main():
    N = int(input())
    K = list(map(int, input().split()))

    total_sum = sum(K)
    half_sum = total_sum // 2

    dp = [0] * (half_sum + 1)

    for k in K:
        for j in range(half_sum, k - 1, -1):
            dp[j] = max(dp[j], dp[j - k] + k)

    group_A = dp[half_sum]
    group_B = total_sum - group_A

    print(max(group_A, group_B))

if __name__ == '__main__':
    main()