# 入力の読み取り
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = [-1] * M

for j in range(M):
    for i in range(N):
        if B[j] >= A[i]:
            result[j] = i + 1
            break

for res in result:
    print(res)