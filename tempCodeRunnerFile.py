from collections import defaultdict
import heapq

Q = int(input())

plants = defaultdict(int)
heights = []

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        plants[0] += 1
        heapq.heappush(heights, 0)
    elif query[0] == '2':
        height = int(query[1])
        if plants[0] > 0:
            plants[height] += plants[0]
            plants[0] = 0
            heapq.heappush(heights, height)
    elif query[0] == '3':
        height = int(query[1])
        count = 0
        for h in list(plants.keys()):
            if h >= height:
                count += plants[h]
                plants[h] = 0
        print(count)