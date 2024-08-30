N, K = map(int, input().split())
A = list(map(int, input().split()))
sub = A[-K:]
A = A[:-K]
A = sub + A
print(' '.join(map(str, A)))