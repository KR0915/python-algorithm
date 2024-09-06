A, B, C, X, Y = map(int, input().split())

cost_direct = A * X + B * Y

cost_ab_only = 2 * C * max(X, Y)

cost_mix = 2 * C * min(X, Y) + A * max(0, X - Y) + B * max(0, Y - X)

min_cost = min(cost_direct, cost_ab_only, cost_mix)

print(min_cost)