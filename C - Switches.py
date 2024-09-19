def count_switch_combinations(N, M, switches, p):
    count = 0
    for bit in range(1 << N):
        all_on = True
        for i in range(M):
            on_count = 0
            for s in switches[i]:
                if bit & (1 << (s - 1)):
                    on_count += 1
            if on_count % 2 != p[i]:
                all_on = False
                break
        if all_on:
            count += 1
    return count

# 入力の受け取り
N, M = map(int, input().split())
switches = []
for _ in range(M):
    data = list(map(int, input().split()))
    switches.append(data[1:])
p = list(map(int, input().split()))

# 結果の出力
print(count_switch_combinations(N, M, switches, p))