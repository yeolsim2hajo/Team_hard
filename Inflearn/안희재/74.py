graph = {1: [2, 3, 4],
		2: [1, 3, 4, 5, 6],
		3: [1, 2, 7],
		4: [1, 2, 5, 6],
		5: [2, 4, 6, 7],
		6: [2, 4, 5, 7],
		7: [3, 5, 6]} 

start, end = [int(i) for i in input().split()]
queue = [start]
visited = []

def sol(n, visited):
	if n[-1] == end:
		return len(visited)
	
	if n[-1] in visited:
		return len(visited)
	
	visited.append(n[-1])
	length = 0
	
	for next_node in graph[n[-1]]:
		n.append(next_node)
		length = max(length, sol(n, visited))
		queue.pop(-1)
	return length

print(sol(queue, visited))