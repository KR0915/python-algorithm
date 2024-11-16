N, K = map(int, input().split())
S = list(input())
counter = 0

for i in range(N - K + 1):
    if S[i:i + K] == ['O'] * K:
        S[i:i + K] = ['X'] * K
        counter += 1

print(counter)