#230227
# Kruskal
# V, E = map(int, input().split())
# link_info = [list(map(int,input().split())) for _ in range(E)]
# link_info.sort(key= lambda x: x[2])
# root_of = list(range(V+1))
# rank_of = [0] * (V+1)
# cnt = total = 0
# def find(node):
#     if root_of[node] != node:
#         root_of[node] = find(root_of[node])
#     return root_of[node]
#
# def link(node1, node2, value):
#     global cnt, total
#     if root_of[node1] == root_of[node2]:
#         return
#     cnt += 1
#     total += value
#     if rank_of[node1] > rank_of[node2]:
#         root_of[node2] = root_of[node1]
#     else:
#         root_of[node1] = root_of[node2]
#         if rank_of[node1] == rank_of[node2]:
#             rank_of[node2] += 1
#
# def union(node1, node2, value):
#     link(find(node1), find(node2), value)
#
# for i in range(E):
#     union(*link_info[i])
#     if cnt == V - 1:
#         break
# print(total)


#
# V, E = map(int, input().split())
# link_info = [list(map(int,input().split())) for _ in range(E)]
# link_info.sort(key= lambda x: x[2])
# root_of = list(range(V+1))
# cnt = total = 0
# def find(node):
#     if root_of[node] == node:
#         return node
#     result = find(root_of[node])
#     root_of[node] = result
#     return result
#
# def union(node1, node2, value):
#     global cnt, total
#     root1, root2 = find(node1), find(node2)
#     if root1 == root2:
#         return
#     cnt += 1
#     total += value
#     root_of[root1] = root2
#
# for i in range(E):
#     union(*link_info[i])
#     if cnt == V - 1:
#         break
# print(total)


#
# def mst():
#     V, E = map(int, input().split())
#     link_info = [list(map(int, input().split())) for _ in range(E)]
#     link_info.sort(key=lambda x: x[2])
#     root_of = list(range(V + 1))
#     cnt = total = 0
#
#     def find(node):
#         if root_of[node] != node:
#             root_of[node] = find(root_of[node])
#         return root_of[node]
#
#     def union(node1, node2, value):
#         nonlocal cnt, total
#         root1, root2 = find(node1), find(node2)
#         if root1 == root2:
#             return
#         cnt += 1
#         total += value
#         root_of[root1] = root2
#
#     for i in range(E):
#         union(*link_info[i])
#         if cnt == V - 1:
#             return total
# print(mst())

#
V, E = map(int, input().split())
link_info = [list(map(int,input().split())) for _ in range(E)]
link_info.sort(key= lambda x: x[2])
root_of = list(range(V+1))
cnt = total = 0
def find(node):
    if root_of[node] != node:
        root_of[node] = find(root_of[node])
    return root_of[node]

def union(node1, node2, value):
    global cnt, total
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return
    cnt += 1
    total += value
    root_of[root1] = root2

for i in range(E):
    union(*link_info[i])
    if cnt == V - 1:
        break
print(total)


# Prim
from heapq import heappop, heappush
V, E = map(int, input().split())
link_info = [[] for _ in range(V+1)]
priority_q = []

for _ in range(E):
    node1, node2, value = list(map(int, input().split()))
    if node1 == 1:
        heappush(priority_q, (value, node2))
    elif node2 == 1:
        heappush(priority_q, (value, node1))
    else:
        link_info[node1].append((value, node2))
        link_info[node2].append((value, node1))

visited = [False] * (V+1)
visited[1] = True
cnt = total = 0
while cnt < V - 1:
    value, destination = heappop(priority_q)
    if not visited[destination]:
        cnt += 1
        total += value
        visited[destination] = True
        for line_info in link_info[destination]:
            heappush(priority_q, line_info)

print(total)