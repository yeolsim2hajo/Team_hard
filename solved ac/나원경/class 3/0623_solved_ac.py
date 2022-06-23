#1992 쿼드트리
# N = int(input())
# video = [input() for _ in range(N)]
# answer = []
# def dfs(number):
#     if number == 1:
#         return
#     dfs(number//2)
#     for x in range(0,number)
#
# for j in range(0,N,N//2):
#     for i in range(0,N,N//2):
#         dfs(N)
# print('(', *answer, ')', sep='')


#7662 이중 우선순위 큐 - 삽입정렬 이용 - 시간 초과
# import sys
# from collections import deque
#
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N = int(input())
#     q = deque()
#     length = 0
#     for i in range(N):
#         calc = new_input().split()
#         calc[1] = int(calc[1])
#         if calc[0] == 'I':
#             for j in range(length-1,-1,-1):
#                 if q[j] <= calc[1]:
#                     q.insert(j+1, calc[1])
#                     break
#             else:
#                 q.appendleft(calc[1])
#             length += 1
#         elif q:
#             length -= 1
#             if calc[1] == -1:
#                 q.popleft()
#             else:
#                 q.pop()
#     if length:
#         print(q[-1], q[0])
#     else:
#         print('EMPTY')


# q 두 개
# import sys, heapq
#
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N = int(input())
#     min_q = []
#     max_q = []
#     length = 0
#     for i in range(N):
#         calc = new_input().split()
#         calc[1] = int(calc[1])
#         if calc[0] == 'I':
#             heapq.heappush(min_q, calc[1])
#             heapq.heappush(max_q, -calc[1])
#             length += 1
#         elif length:
#             length -= 1
#             if calc[1] == -1:
#                 min_val = heapq.heappop(min_q)
#                 max_q.remove(-min_val)
#                 heapq.heapify(max_q)
#             else:
#                 max_val = heapq.heappop(max_q)
#                 min_q.remove(-max_val)
#                 heapq.heapify(min_q)
#     if length:
#         print(-max_q[0], min_q[0])
#     else:
#         print('EMPTY')


# largest 이용 - 시간 초과
# import sys, heapq
#
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N = int(input())
#     q = []
#     length = 0
#     for i in range(N):
#         calc = new_input().split()
#         calc[1] = int(calc[1])
#         if calc[0] == 'I':
#             heapq.heappush(q, calc[1])
#             length += 1
#         elif length:
#             length -= 1
#             if calc[1] == -1:
#                 heapq.heappop(q)
#             else:
#                 max_val = heapq.nlargest(1,q)
#                 q.remove(*max_val)
#     if length:
#         print(*heapq.nlargest(1,q), q[0])
#     else:
#         print('EMPTY')


#9019 DSLR

# bfs - 시간 초과
# T = int(input())
# for _ in range(T):
#     initial, final = map(int, input().split())
#
#     def bfs():
#         q = [(initial,'')]
#         def change():
#             D = (number * 2)% 10000
#             S = number-1 if number > 1 else 9999
#             str_number = str(number)
#             L = int(str_number[1:] + str_number[0])
#             R = int(str_number[-1] + str_number[:-1])
#
#             q.append((D, command + 'D'))
#             q.append((S, command + 'S'))
#             q.append((L, command + 'L'))
#             q.append((R, command + 'R'))
#         while q:
#             number, command = q.pop(0)
#             if number == final:
#                 print(command)
#                 return
#             change()
#     bfs()


# bfs
# from collections import deque
# T = int(input())
# for _ in range(T):
#     initial, final = map(int, input().split())
#     def bfs():
#         q = deque()
#         q.append((initial,''))
#         while q:
#             number, command = q.popleft()
#             if number == final:
#                 print(command)
#                 return
#             str_number = str(number)
#             change = {
#                 'D': lambda : (number * 2) % 10000,
#                 'S' : lambda : number-1 if number > 1 else 9999,
#                 'L' : lambda : int(str_number[1:] + str_number[0]),
#                 'R' : lambda : int(str_number[-1] + str_number[:-1])
#             }
#             for key in change.keys():
#                 q.append((key, command + change[key]()))
#             print(key, change[key]())
#     bfs()


#9461 파도반 수열
# T = int(input())
# arr = [1,1,1,2,2]
# length = 5
# for _ in range(T):
#     N = int(input())
#     if length < N:
#         while length < N:
#             arr.append(arr[length-1]+arr[length-5])
#             length += 1
#     print(arr[N-1])

