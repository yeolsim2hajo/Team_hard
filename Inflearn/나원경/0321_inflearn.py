#69 골드바흐의 추측 - 모두 출력
# n = int(input())
# ans = []
# small = large = n // 2
# while small >= 2:
#     if small == 2:
#         for number in range(3,large//2+1,2):
#             if large%number == 0:
#                 break
#         else:
#             ans.append([small, large])
#         break
#     elif small%2 == 0:
#         small -= 1
#         large += 1
#     else:
#         for number in range(3,small//2+1,2):
#             if small%number == 0:
#                 break
#         else:
#             ans.append([small,large])
#             for number in range(3,large//2+1,2):
#                 if large%number == 0:
#                     ans.pop()
#                     break
#         small -= 2
#         large += 2
# print(*ans)


#70 행렬 곱하기 - 다시
# ([1,2],[2,4])
# a = input().strip('()')
# n = m = 0
#
# for i in range(len(a)):
#     if a[i:i+2] == '],':
#         n += 1
#         m =
# # b = input()
# # n = len(a)
# # m = len(a[0])
# # if len(b) != m or len(b[0]) != n:
# #     print(-1)
# # else:
#
#
#
# # a = a.split(',')
# print(a)


#71 깊이 우선 탐색
# graph = {'E': set(['D','A']),
#          'F': set(['D']),
#          'A': set(['E', 'C','B']),
#          'B': set(['A']),
#          'C': set(['A']),
#          'D': set(['E','F'])}
#
# def dfs(graph,start):
#     visited = []
#     stack = [start]
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             for value in graph[n]:
#                 stack.append(value)
#     return visited
# print(dfs(graph,'E'))

# 오른쪽 왼쪽은 set 사용x
# 리스트로 구현 - 나중에

