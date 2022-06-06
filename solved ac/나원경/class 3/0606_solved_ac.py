#1074 Z
# N, row, col = map(int,input().split())
# n = 2**(N-1)
# cnt = x = y = 0
# while n >= 1:
#     if n == 1:
#         for dy,dx in (0,0),(0,1),(1,0),(1,1):
#             if y+dy == row and x+dx == col:
#                 n -= 1
#                 break
#             cnt += 1
#     else:
#         if row < y+n:
#             if col >= x+n:
#                 cnt += n**2
#                 x += n
#         elif col < x+n:
#             cnt += (n**2) * 2
#             y += n
#         else:
#             cnt += (n**2) * 3
#             y += n
#             x += n
#         n //= 2
#
# print(cnt)


#1107 리모컨
# N = input()
# M = int(input())
# number = int(N)
# if M:
#     numbers = set(map(int,input().split()))
# length = len(N)
# min_move = abs(number - 100)
# def find_channel(arg=0,result=''):
#     global dif
#     if dif == 0:
#         return
#     if result not in {'0', ''} and result[0] == '0':
#         return
#     if arg == length:
#         if abs(int(result) - number) < dif:
#             dif = abs(int(result) - number)
#         return
#     for i in buttons:
#         find_channel(arg+1, result+i)
#
# # 고장난 버튼 없음
# if M == 0:
#     if min_move > length:
#         min_move = length
# # 이동이 필요한 경우
# elif min_move:
#     # 누를 수 있는 버튼
#     buttons = set()
#     for i in range(10):
#         if i not in numbers:
#             buttons.add(str(i))
#     for i in range(length):
#         if N[i] not in buttons:
#             dif = min_move
#             find_channel()
#             min_move = min(min_move, length + dif)
#             break
#     else:
#         min_move = min(min_move, length)
#
# print(min_move)


#1260 DFS와 BFS
# import sys
# N, M, V = map(int,input().split())
# new_input = sys.stdin.readline
# link = [[] for _ in range(N+1)]
# for _ in range(M):
#     y,x = map(int,new_input().split())
#     link[y].append(x)
#     link[x].append(y)
#     link[y].sort()
#     link[x].sort()
# def dfs(start):
#     for i in link[start]:
#         if visited[i] is False:
#             visited[i] = True
#             answer.append(i)
#             dfs(i)
# def bfs(start):
#     q = link[start][:]
#     while q:
#         number = q.pop(0)
#         if visited[number] is False:
#             visited[number] = True
#             answer.append(number)
#             q.extend(link[number])
#
# visited = [False] * (N+1)
# visited[V] = True
# answer = [V]
# dfs(V)
# print(*answer)
# visited = [False] * (N+1)
# visited[V] = True
# answer = [V]
# bfs(V)
# print(*answer)
