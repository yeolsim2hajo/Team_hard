graph = {'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])}

start, end = [i for i in input().split()]
    
queue = [start]
visited = [start]
    
def solution():
    count = -1

    while len(queue)!=0:
        count += 1
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)
            if node == end:
                return count
            # 만약, node가 end가 아니라면 아래 작업으로 다음 q추가해줌
            # visited까지 추가해줘서, q에 또 추가 안하도록 예방!
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.append(next_node)
                    queue.append(next_node)

print(solution())