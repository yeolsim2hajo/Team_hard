#230112
# bfs - 시간 초과
# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# levels = [set() for _ in range(N)]
# visited[R] = True
# levels[0].add(R)
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     while i < len(node_info[root]):
#         node = node_info[root][i]
#         if not visited[node]:
#             visited[node] = True
#             levels[level].add(node)
#             q.append((node, level))
#             i += 1
#         else:
#             node_info[root].remove(node)
# for _ in range(Q):
#     new_root = int(new_input())
#     cnt = 1
#     q.append(new_root)
#     while q:
#         node = q.popleft()
#         cnt += len(node_info[node])
#         q.extend(node_info[node])
#     print(cnt)

# remove => pop - 55%에서 시간초과
# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# # levels = [set() for _ in range(N)]
# visited[R] = True
# # levels[0].add(R)
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     while i < len(node_info[root]):
#         node = node_info[root][i]
#         if not visited[node]:
#             visited[node] = True
#             # levels[level].add(node)
#             q.append((node, level))
#             i += 1
#         else:
#             node_info[root].pop(i)
# for _ in range(Q):
#     new_root = int(new_input())
#     cnt = 1
#     q.append(new_root)
#     while q:
#         node = q.popleft()
#         cnt += len(node_info[node])
#         q.extend(node_info[node])
#     print(cnt)



#230114
# 유니온 파인드

## 55에서 recursion Error

# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# visited[R] = True
# high_level, components = [[] for _ in range(201)], [1] * (N+1)
# max_level = 0
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     while i < len(node_info[root]):
#         node = node_info[root][i]
#         if not visited[node]:
#             visited[node] = True
#             q.append((node, level))
#             i += 1
#         else:
#             node_info[root].pop(i)
#     if level > max_level:
#         max_level = level
#     if level >= 500:
#         quot = level//500
#         if not high_level[quot]:
#             high_level[quot].append((root, level-1))
#
# def dfs(now, level, limit=499):
#     if level == limit:
#         return
#     sub_tree = node_info[now]
#     for child in sub_tree:
#         dfs(child, level+1)
#     for i in sub_tree:
#         components[now] += components[i]
#
# # print(high_level)
#
# if max_level >= 500:
#     for i in range(max_level//500, 0, -1):
#         print(high_level)
#         root, level = high_level[i][0]
#         # print(root, level)
#         dfs(root, level, level + 499)
# dfs(R, 0)
#
# for _ in range(Q):
#     new_root = int(new_input())
#     print(components[new_root])



# bfs + union find - 틀림
# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# visited[R] = True
# parent, components = [0] * (N+1), [1] * (N+1)
# high_level = set()
# max_level = 0
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     child = node_info[root]
#     while i < len(child):
#         node = child[i]
#         if not visited[node]:
#             visited[node] = True
#             q.append((node, level))
#             i += 1
#             parent[node] = root
#         else:
#             node_info[root].pop(i)
#
#     if not child:
#         # if level > max_level:
#         #     max_level = level
#         #     high_level = [root]
#         # elif level == max_level:
#         high_level.add(parent[root])
#
# # print(parent)
# # print(node_info)
# # print(high_level)
# q = deque()
# # for node in high_level:
# #     root = parent[node]
# #     components[root] += components[node]
# #     q.append(root)
# q.extend(high_level)
#
# while q:
#     node = q.popleft()
#     for i in node_info[node]:
#         components[node] += components[i]
#     if node != R:
#         root = parent[node]
#         q.append(root)
#     else:
#         break
# #     print(node, parent, components)
# # print(components)
#
# for _ in range(Q):
#     new_root = int(new_input())
#     print(components[new_root])


# bfs - union find - 틀린 것 정리함
# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# visited[R] = True
# parent, components = [0] * (N+1), [1] * (N+1)
# high_level = set()
# max_level = 0
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     child = node_info[root]
#     while i < len(child):
#         node = child[i]
#         if not visited[node]:
#             visited[node] = True
#             q.append((node, level))
#             i += 1
#             parent[node] = root
#             # print(node, root, parent)
#         else:
#             node_info[root].pop(i)
#
#     if not child:
#         high_level.add(parent[root])
#
# q = deque()
# q.extend(high_level)
#
# while True:
#     node = q.popleft()
#     for i in node_info[node]:
#         components[node] += components[i]
#     if node == R:
#         break
#     root = parent[node]
#     q.append(root)
#
# for _ in range(Q):
#     new_root = int(new_input())
#     print(components[new_root])


#230115
# bfs - 5%에서 틀림
# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# visited[R] = True
# parent, components = [0] * (N+1), [1] * (N+1)
# high_level = []
# max_level = 0
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     child = node_info[root]
#     while i < len(child):
#         node = child[i]
#         if not visited[node]:
#             visited[node] = True
#             q.append((node, level))
#             i += 1
#             parent[node] = root
#             # print(node, root, parent)
#         else:
#             node_info[root].pop(i)
#
#         if not child:
#             high_level.append(root)
#
# q = deque()
# q.extend(high_level[::-1])
# visited = [False] * (N+1)
# while True:
#     node = q.popleft()
#     if not visited[node]:
#         visited[node] = True
#         for i in node_info[node]:
#             components[node] += components[i]
#         # print(node, components)
#         if node == R:
#             break
#         root = parent[node]
#         q.append(root)
#
# for _ in range(Q):
#     new_root = int(new_input())
#     print(components[new_root])



# heap 사용
# import sys
# from collections import deque
# from heapq import heapify, heappop, heappush
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# visited[R] = True
# parent, components = [0] * (N+1), [1] * (N+1)
# high_level = []
# max_level = 0
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     child = node_info[root]
#     while i < len(child):
#         node = child[i]
#         if not visited[node]:
#             visited[node] = True
#             q.append((node, level))
#             i += 1
#             parent[node] = root
#             # print(node, root, parent)
#         else:
#             node_info[root].pop(i)
#
#     high_level.append((-level+1, root))
#
# heap = high_level[:]
# heapify(heap)
# visited = [False] * (N+1)
# while True:
#     level, node = heappop(heap)
#     if not visited[node]:
#         visited[node] = True
#         for i in node_info[node]:
#             components[node] += components[i]
#         # print(node, components)
#         if level == 0:
#             break
#         root = parent[node]
#         heappush(heap, (level+1, root))
#
# for _ in range(Q):
#     new_root = int(new_input())
#     print(components[new_root])


# 정리
# def change_child():
#     from collections import deque
#     q, visited = deque([(R,0)]),[False] * (N+1)
#     visited[R] = True
#     while q:
#         root, level = q.popleft()
#         level += 1
#         i = 0
#         child_arr = child[root]
#         while i < len(child_arr):
#             node = child_arr[i]
#             if not visited[node]:
#                 q.append((node, level))
#                 i += 1
#                 parent[node] = root
#                 visited[node] = True
#             else:
#                 child[root].pop(i)
#
#         heap.append((-level+1, root))
#
# def change_components():
#     from heapq import heapify, heappop, heappush
#     visited = [False] * (N+1)
#     heapify(heap)
#     while True:
#         level, node = heappop(heap)
#         if not visited[node]:
#             visited[node] = True
#             for i in child[node]:
#                 components[node] += components[i]
#             if level == 0:
#                 return
#             root = parent[node]
#             heappush(heap, (level+1, root))
#
# import sys
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# child, heap = [[] for _ in range(N+1)], []
# parent, components = [0] * (N + 1), [1] * (N + 1)
#
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     child[node_1].append(node_2)
#     child[node_2].append(node_1)
#
# change_child()
# change_components()
#
# for _ in range(Q):
#     new_root = int(new_input())
#     print(components[new_root])


# main
# def main():
#     def change_child():
#         from collections import deque
#         q, visited = deque([(R, 0)]), [False] * (N + 1)
#         visited[R] = True
#         while q:
#             root, level = q.popleft()
#             level += 1
#             i = 0
#             child_arr = child[root]
#             while i < len(child_arr):
#                 node = child_arr[i]
#                 if not visited[node]:
#                     q.append((node, level))
#                     i += 1
#                     parent[node] = root
#                     visited[node] = True
#                 else:
#                     child[root].pop(i)
#
#             heap.append((-level + 1, root))
#
#     def change_components():
#         from heapq import heapify, heappop, heappush
#         visited = [False] * (N + 1)
#         heapify(heap)
#         while True:
#             level, node = heappop(heap)
#             if not visited[node]:
#                 visited[node] = True
#                 for i in child[node]:
#                     components[node] += components[i]
#                 if level == 0:
#                     return
#                 root = parent[node]
#                 heappush(heap, (level + 1, root))
#
#     import sys
#
#     new_input = sys.stdin.readline
#     N, R, Q = map(int, new_input().split())
#     child, heap = [[] for _ in range(N + 1)], []
#     parent, components = [0] * (N + 1), [1] * (N + 1)
#
#     for _ in range(N - 1):
#         node_1, node_2 = map(int, new_input().split())
#         child[node_1].append(node_2)
#         child[node_2].append(node_1)
#
#     change_child()
#     change_components()
#
#     for _ in range(Q):
#         new_root = int(new_input())
#         print(components[new_root])
#
# main()


# main +
# def main():
#     def change_child():
#         from collections import deque
#         q, visited = deque([(R, 0)]), [False] * (N + 1)
#         visited[R] = True
#         while q:
#             root, level = q.popleft()
#             level += 1
#             i = 0
#             child_arr = child[root]
#             while i < len(child_arr):
#                 node = child_arr[i]
#                 if not visited[node]:
#                     q.append((node, level))
#                     i += 1
#                     parent[node] = root
#                     visited[node] = True
#                 else:
#                     child[root].pop(i)
#
#             heap.append((-level + 1, root))
#
#     def change_components():
#         from heapq import heapify, heappop, heappush
#         visited, components = [False] * (N + 1), [1] * (N + 1)
#         heapify(heap)
#         while True:
#             level, node = heappop(heap)
#             if not visited[node]:
#                 visited[node] = True
#                 for i in child[node]:
#                     components[node] += components[i]
#                 if level == 0:
#                     for _ in range(Q):
#                         new_root = int(new_input())
#                         print(components[new_root])
#                     return
#                 root = parent[node]
#                 heappush(heap, (level + 1, root))
#
#     import sys
#
#     new_input = sys.stdin.readline
#     N, R, Q = map(int, new_input().split())
#     child, parent, heap = [[] for _ in range(N + 1)], [0] * (N + 1), []
#     for _ in range(N - 1):
#         node_1, node_2 = map(int, new_input().split())
#         child[node_1].append(node_2)
#         child[node_2].append(node_1)
#
#     change_child()
#     change_components()
#
# main()


#
# def main():
#     def change_child():
#         from collections import deque
#         q, visited = deque([(R, 0)]), [False] * (N + 1)
#         visited[R] = True
#         while q:
#             root, level = q.popleft()
#             level += 1
#             i = 0
#             child_arr = child[root]
#             while i < len(child_arr):
#                 node = child_arr[i]
#                 if not visited[node]:
#                     q.append((node, level))
#                     i += 1
#                     parent[node] = root
#                     visited[node] = True
#                 else:
#                     child[root].pop(i)
#
#             heappush(heap, (-level + 1, root))
#
#     def change_components():
#         visited, components = [False] * (N + 1), [1] * (N + 1)
#         while True:
#             level, node = heappop(heap)
#             if not visited[node]:
#                 visited[node] = True
#                 for i in child[node]:
#                     components[node] += components[i]
#                 if level == 0:
#                     for _ in range(Q):
#                         new_root = int(new_input())
#                         print(components[new_root])
#                     return
#                 root = parent[node]
#                 heappush(heap, (level + 1, root))
#
#     import sys
#     from heapq import heappop, heappush
#     new_input = sys.stdin.readline
#     N, R, Q = map(int, new_input().split())
#     child, parent, heap = [[] for _ in range(N + 1)], [0] * (N + 1), []
#     for _ in range(N - 1):
#         node_1, node_2 = map(int, new_input().split())
#         child[node_1].append(node_2)
#         child[node_2].append(node_1)
#
#     change_child()
#     change_components()
#
# main()


# levels
def main():
    def change_child():
        nonlocal max_level
        from collections import deque
        q, visited = deque([(R, 0)]), [False] * (N + 1)
        visited[R] = True
        length = 0
        while q:
            root, level = q.popleft()
            new_level = level+1
            i = 0
            child_arr = child[root]
            while i < len(child_arr):
                node = child_arr[i]
                if not visited[node]:
                    q.append((node, new_level))
                    i += 1
                    visited[node] = True
                else:
                    child[root].pop(i)

            if length <= level:
                levels.append([])
                length += 1
            levels[level].append(root)
            if level > max_level:
                max_level = level

    def change_components():
        components = [1] * (N + 1)
        for level in range(max_level, -1, -1):
            for node in levels[level]:
                for i in child[node]:
                    components[node] += components[i]
        for _ in range(Q):
            new_root = int(new_input())
            print(components[new_root])

    import sys
    new_input = sys.stdin.readline
    N, R, Q = map(int, new_input().split())
    child, levels = [[] for _ in range(N + 1)], []
    max_level = 0
    for _ in range(N - 1):
        node_1, node_2 = map(int, new_input().split())
        child[node_1].append(node_2)
        child[node_2].append(node_1)

    change_child()
    change_components()

main()