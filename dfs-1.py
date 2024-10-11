def dfs(graph, vertex, visited, discovery_time, finish_time, time):
    visited[vertex] = True
    time[0] += 1
    discovery_time[vertex] = time[0]
    
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, discovery_time, finish_time, time)
    
    time[0] += 1
    finish_time[vertex] = time[0]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n):
        u = int(data[index])
        k = int(data[index + 1])
        neighbors = list(map(int, data[index + 2: index + 2 + k]))
        graph[u].extend(neighbors)
        index += 2 + k
    
    visited = [False] * (n + 1)
    discovery_time = [0] * (n + 1)
    finish_time = [0] * (n + 1)
    time = [0]
    
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            dfs(graph, vertex, visited, discovery_time, finish_time, time)
    
    for vertex in range(1, n + 1):
        print(vertex, discovery_time[vertex], finish_time[vertex])

if __name__ == "__main__":
    main()