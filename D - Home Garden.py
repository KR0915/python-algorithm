from queue import deque

Q = int(input())

que = deque()
current_time = 0

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        que.append(current_time)
    elif query[0] == '2':
        current_time += int(query[1])
    else:
        H = int(query[1])
        count = 0
        while que and current_time - que[0] >= H:
            que.popleft()
            count += 1
        print(count)