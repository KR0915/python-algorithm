from collections import Counter
A=list(map(int,input().split()))
count = Counter(A)
pairs = sum(v // 2 for v in count.values())
print(pairs)