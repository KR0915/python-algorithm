N = int(input())
day = []
for _ in range(N):
    q, r = map(int, input().split())
    day.append((q, r))

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    q, r = day[t-1]
    if d % q <= r:
        next_collection_day = d + (r - d % q)
    else:
        next_collection_day = d + (q - d % q) + r
    print(next_collection_day)