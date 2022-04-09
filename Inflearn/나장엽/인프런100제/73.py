graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

start, end = list(input().split())
    
que = [start]
visited = [start]
    
def solution():
    count = 0

    while len(queue)!=0:
        cnt += 1
        size = len(que)

        for i in range(size):
            now = que.pop(0)
            if now == end:
                return cnt

            for next in graph[now]:
                if next not in visited:
                    visited.append(next)
                    queue.append(next)

print(solution())
