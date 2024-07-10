N,K=map(int,input().split())
A=list(map(int,input().split()))

A.sort()
    
min_diff = float('inf')

for start in range(K + 1):
    end = N - (K - start)
    if end <= N:
        current_min = A[start]
        current_max = A[end - 1]
        min_diff = min(min_diff, current_max - current_min)
        
print(min_diff)