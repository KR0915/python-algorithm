from collections import deque, defaultdict

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    graph = defaultdict(list)
    for _ in range(N - 1):
        A = int(data[idx])
        idx += 1
        B = int(data[idx])
        idx += 1
        graph[A].append(B)
        graph[B].append(A)
    
    V = []
    for _ in range(K):
        V.append(int(data[idx]))
        idx += 1
    
    # 任意の指定された頂点からBFSを行う
    dist = bfs(V[0], graph, N)
    
    # 指定された頂点の中で最も遠い頂点を探す
    farthest_node = V[0]
    max_dist = 0
    for v in V:
        if dist[v] > max_dist:
            max_dist = dist[v]
            farthest_node = v
    
    # 最も遠い頂点から再度BFSを行う
    dist = bfs(farthest_node, graph, N)
    
    # 指定された頂点の中で最も遠い頂点を探す
    max_dist = 0
    for v in V:
        if dist[v] > max_dist:
            max_dist = dist[v]
    
    # 最小の部分木の頂点数は、最も遠い距離 + 1
    print(max_dist + 1)

if __name__ == "__main__":
    solve()