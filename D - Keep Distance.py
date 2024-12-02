from itertools import combinations

N, M = map(int, input().split())

valid_sequences = []
for comb in combinations(range(1, M + 1), N):
    if all(comb[i] + 10 <= comb[i + 1] for i in range(N - 1)):
        valid_sequences.append(comb)

print(len(valid_sequences))
for seq in valid_sequences:
    print(' '.join(map(str, seq)))