N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)
ans = sorted_A[-2]
for i in range(N):
    if A[i] == ans:
        print(i + 1)
        break
