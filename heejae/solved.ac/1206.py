    from collections import deque
    
    
    def dfs(v):
        visited_dfs[v] = True
        order_dfs.append(v)
        for i in graph[v]:
            if not visited_dfs[i]:
                dfs(i)
    
    
    def bfs(v):
        visited_bfs[v] = True
        order_bfs.append(v)
        queue = deque([v])
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited_bfs[i]:
                    visited_bfs[i] = True
                    order_bfs.append(i)
                    queue.append(i)
    
    
    if __name__ == "__main__":
        n, m, start = map(int, input().split())
        graph = []
        for _ in range(n+1):
            graph.append([])
    
        for _ in range(m):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[x].sort()
            graph[y].append(x)
            graph[y].sort()
    
    
        visited_dfs = [False] * (n+1)
        order_dfs = []
        visited_bfs = [False] * (n+1)
        order_bfs = []
    
        dfs(start)
        print(*order_dfs)
        bfs(start)
        print(*order_bfs)