graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0) # q.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(bfs(graph, 'E'))