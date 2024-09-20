N, M = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) <= M:
    print('infinite')
else:
    low, high = 0, max(A)
    while low < high:
        mid = (low + high + 1) // 2
        total = sum(min(mid, a) for a in A)
            
        if total <= M:
            low = mid
        else:
            high = mid - 1
            
    print(low)