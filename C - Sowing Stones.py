N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

required_stones = [1] * N

stones = [0] * N
for i in range(M):
    stones[X[i] - 1] = A[i]

operations = 0
for i in range(N - 1):
    if stones[i] > required_stones[i]:
        excess = stones[i] - required_stones[i]
        stones[i] -= excess
        stones[i + 1] += excess
        operations += excess

if stones[N - 1] != required_stones[N - 1]:
    print(-1)
else:
    print(operations)