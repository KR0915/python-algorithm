N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]

X = [(L + R) // 2 for L, R in LR]

total = sum(X)

for i, (L, R) in enumerate(LR):
    if total == 0:
        break
    elif total > 0 and X[i] > L:
        adjust = min(total, X[i] - L)
        X[i] -= adjust
        total -= adjust
    elif total < 0 and X[i] < R:
        adjust = min(-total, R - X[i])
        X[i] += adjust
        total += adjust

if total == 0:
    print(" ".join(map(str, X)))
else:
    print("No")