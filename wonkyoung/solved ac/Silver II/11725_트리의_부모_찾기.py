#230116

'''
7
6 3
3 5
4 1
2 4
1 6
4 7
'''

# 틀림
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# parent = [i for i in range(N+1)]
# def find_parent(node1, node2):
#     print(node1, node2, parent[node1])
#     if node1 == 1:
#         parent[node2] = 1
#         return
#     top = parent[node1]
#     if top == parent[top]:
#
#     if node2 != parent[node1] != node1:
#         return find_parent(parent[node1], node1)
#     parent[node1] = node2
#
# for _ in range(N-1):
#     node1, node2 = map(int, new_input().split())
#     find_parent(node1, node2)
#     find_parent(node2, node1)
# for i in range(2, N):
#     print(parent[i])


# bfs
# import sys
# from collections import deque
# new_input = sys.stdin.readline
# N = int(new_input())
# parent = [-1] * (N+1)
# node_list = [[] for i in range(N+1)]
# for _ in range(N-1):
#     node1, node2 = map(int, new_input().split())
#     node_list[node1].append(node2)
#     node_list[node2].append(node1)
#
# visited = [False] * (N+1)
# visited[1] = True
# q = deque()
# for child in node_list[1]:
#     q.append((1, child))
# while q:
#     top, bottom = q.popleft()
#     if not visited[bottom]:
#         visited[bottom] = True
#         parent[bottom] = top
#         for child in node_list[bottom]:
#             q.append((bottom, child))
# for i in range(2, N+1):
#     print(parent[i])


# sep 사용
# import sys
# from collections import deque
# new_input = sys.stdin.readline
# N = int(new_input())
# parent = [-1] * (N+1)
# node_list = [[] for i in range(N+1)]
# for _ in range(N-1):
#     node1, node2 = map(int, new_input().split())
#     node_list[node1].append(node2)
#     node_list[node2].append(node1)
#
# visited = [False] * (N+1)
# visited[1] = True
# q = deque()
# for child in node_list[1]:
#     q.append((1, child))
# while q:
#     top, bottom = q.popleft()
#     if not visited[bottom]:
#         visited[bottom] = True
#         parent[bottom] = top
#         for child in node_list[bottom]:
#             q.append((bottom, child))
# print(*parent[2:], sep='\n')


# 함수화
# import sys
# from collections import deque
# new_input = sys.stdin.readline
# N = int(new_input())
# node_list = [[] for i in range(N+1)]
# for _ in range(N-1):
#     node1, node2 = map(int, new_input().split())
#     node_list[node1].append(node2)
#     node_list[node2].append(node1)
#
# def bfs():
#     visited = [False] * (N+1)
#     visited[1] = True
#     parent = [-1] * (N + 1)
#     q = deque()
#     for child in node_list[1]:
#         q.append((1, child))
#     while q:
#         top, bottom = q.popleft()
#         if not visited[bottom]:
#             visited[bottom] = True
#             parent[bottom] = top
#             for child in node_list[bottom]:
#                 q.append((bottom, child))
#     for i in range(2, N+1):
#         print(parent[i])
# bfs()


# 함수화2
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     node_list = [[] for i in range(N+1)]
#     for _ in range(N-1):
#         node1, node2 = map(int, new_input().split())
#         node_list[node1].append(node2)
#         node_list[node2].append(node1)
#
#     def bfs():
#         from collections import deque
#         visited = [False] * (N+1)
#         visited[1] = True
#         parent = [-1] * (N + 1)
#         q = deque()
#         def append_element(index, arr):
#             for child in arr:
#                 q.append((index, child))
#         append_element(1, node_list[1])
#         while q:
#             top, bottom = q.popleft()
#             if not visited[bottom]:
#                 visited[bottom] = True
#                 parent[bottom] = top
#                 append_element(bottom, node_list[bottom])
#         for i in range(2, N+1):
#             print(parent[i])
#     bfs()
#
# main()


# 인자 조절
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     node_list = [[] for i in range(N+1)]
#     for _ in range(N-1):
#         node1, node2 = map(int, new_input().split())
#         node_list[node1].append(node2)
#         node_list[node2].append(node1)
#
#     def bfs():
#         from collections import deque
#         visited = [False] * (N+1)
#         visited[1] = True
#         parent = [-1] * (N + 1)
#         q = deque()
#         def append_element(index):
#             for child in node_list[index]:
#                 q.append((index, child))
#         append_element(1)
#         while q:
#             top, bottom = q.popleft()
#             if not visited[bottom]:
#                 visited[bottom] = True
#                 parent[bottom] = top
#                 append_element(bottom)
#         for i in range(2, N+1):
#             print(parent[i])
#     bfs()
#
# main()
