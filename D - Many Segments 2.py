N,M=map(int,input().split())
intervals=[]
for _ in range(N):
    L,R=map(int,input().split())
    intervals.append((L,R))

def count_valid_pairs(N, M, intervals):
    invalid = [[False] * (M + 1) for _ in range(M + 1)]
    
    for L, R in intervals:
        for l in range(1, L + 1):
            for r in range(R, M + 1):
                invalid[l][r] = True
    
    valid_count = 0
    for l in range(1, M + 1):
        for r in range(l, M + 1):
            if not invalid[l][r]:
                valid_count += 1
    
    return valid_count

print(count_valid_pairs(N, M, intervals))