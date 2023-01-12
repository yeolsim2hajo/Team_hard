#221224
# bfs - 메모리 초과
# import sys
# from collections import deque
# new_input = sys.stdin.readline
# N = int(new_input())
# schedule = [list(map(int, new_input().split())) for _ in range(N)]
# q = deque()
# for i in range(schedule[0][0]):
#     during, profit = schedule[i]
#     q.append((i+during, profit))
# max_total = 0
# while q:
#     next, total = q.popleft()
#     if next < N:
#         max_total = max(max_total, total)
#         during, profit = schedule[next]
#         q.append((next+during, total + profit))
#         if during > 1:
#             q.append((next + 1, total))
#     elif next == N:
#         max_total = max(max_total, total)
# print(max_total)



# dp - 뒤에서부터
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# schedule = [list(map(int, new_input().split())) for _ in range(N)]
# max_total = [0] * (N+1)
# max_next = max_i = 0
# for i in range(N-1, -1, -1):
#     during, profit = schedule[i]
#     next = i + during
#     if next <= N:
#         new_val = max_total[next] + profit if max_i < next else max_next + profit
#         if max_total[i] <= new_val:
#             max_total[i] = new_val
#             if max_next <= new_val:
#                 max_next = new_val
#                 max_i = i
# print(max_total)
# print(max_next)


#221231
#dp - 앞에서부터
# X
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# schedule = [list(map(int, new_input().split())) for _ in range(N)]
# max_profit = [0] * (N+1)
# for day in range(N):
#     during, profit = schedule[day]
#     next = day+during
#     if next <= N:
#         max_profit[next] = max(max_profit[day]+profit, max_profit[next])
# print(max_profit)


# 뒷 부분 같게 - 시간 초과
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# # schedule = [list(map(int, new_input().split())) for _ in range(N)]
# max_profit = [0] * (N+1)
# max_next = max_i = 0
# for day in range(N):
#     during, profit = map(int, new_input().split())
#     next, new_profit = day+during, max_profit[day]+profit
#     if next <= N and new_profit > max_profit[next]:
#         max_profit[next] = new_profit
#         if
#         for i in range(next, N+1):
#             max_profit[i] = max(new_profit, max_profit[i])
# print(max_profit[-1])


# dp - 앞에서부터
import sys
new_input = sys.stdin.readline
N = int(new_input())
schedule = [list(map(int, new_input().split())) for _ in range(N)]
max_total = [0] * (N+1)
max_next = max_i = max_next_i = 0
for i in range(N):
    during, profit = schedule[i]
    next = i + during
    if next <= N:
        new_val = max_next if max_i <= i else max_total[i]
        if max_total[next] <= new_val + profit:
            max_total[next] = new_val + profit
        if max_next <= new_val:
            max_next = new_val
            max_i, max_next_i = i, next
print(max_total[max_next_i])