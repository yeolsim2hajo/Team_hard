#9094 수학적 호기심
# from sys import stdin
# new_input = stdin.readline
# T = int(new_input())
# for _ in range(T):
#     N, M = map(int, new_input().split())
#     cnt = 0
#     for i in range(1, N-1):
#         son = i**2 + M
#         for j in range(i+1, N):
#             if (son + j**2)%(i*j) == 0:
#                 cnt += 1
#     print(cnt)


#14575 뒤풀이
# import sys
# new_input = sys.stdin.readline
# N, T = map(int, new_input().split())
# min_values = []
# max_values = []
# min_total = max_total = 0
# for _ in range(N):
#     left, right = map(int, new_input().split())
#     min_values.append(left)
#     max_values.append(right)
#     min_total += left
#     max_total += right
#
# if min_total > T or max_total < T:
#     print(-1)
# elif min_total == T:
#     print(max(min_values))
# elif max_total == T:
#     print(max(max_values))
# else:
#     average, remain = divmod(N, T)
#     total = average*N
#     change = []
#     start, end = 0, N-1
#     S = average
#     while True:
#         for i in range(N):
#             if min_values[i] > average:
#                 total += min_values[i] - average
#                 change.append((i,0))
#             elif max_values[i] < average:
#                 total += max_values[i] - average
#                 change.append((i,1))
#         if total < T:
#             pass
#         elif total > T:
#             pass
#         else:
#             S = min(S, average)


#14567 선수과목
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# match = [[] for _ in range(N+1)]
# min_time = [1]*(N+1)
# for _ in range(M):
#     before, after = map(int, new_input().split())
#     match[after].append(before)
# for i in range(1, N+1):
#     if match[i]:
#         max_time = [min_time[j] for j in match[i]]
#         min_time[i] = max(max_time)+1
# print(*min_time[1:])

#함수로 만들기
# def find_min():
#     import sys
#     from collections import deque
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     match = [[] for _ in range(N+1)]
#     min_time = deque([1]*(N+1))
#
#     for _ in range(M):
#         before, after = map(int, new_input().split())
#         match[after].append(before)
#
#     for i in range(1, N+1):
#         if match[i]:
#             max_time = [min_time[j] for j in match[i]]
#             min_time[i] = max(max_time)+1
#
#     min_time.popleft()
#     return min_time
#
# print(*find_min())








