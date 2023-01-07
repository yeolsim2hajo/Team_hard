#230107
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# order = list(map(int, new_input().split()))
# info = [0]
# info.extend([list(map(int, new_input().split())) for _ in range(N-1)])
# visited = [0] * N
# now = order[0]
# for i in range(1, M):
#     next = order[i]
#     if now <= next:
#         start, end = now, next
#     else:
#         start, end = next, now
#     for j in range(start, end):
#         visited[j] += 1
#         # print(i, j, start, end)
#     now = next
# total_cost = 0
# for i in range(1, N):
#     cnt = visited[i]
#     if cnt:
#         ticket, card = cnt * info[i][0], cnt * info[i][1] + info[i][2]
#         total_cost += min(ticket, card)
# # print(visited)
# print(total_cost)


# map - 50점
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# order = list(map(int, new_input().split()))
# info = [0]
# info.extend([list(map(int, new_input().split())) for _ in range(N-1)])
# visited = [0] * N
# now = order[0]
# def plus_one(number):
#     return number+1
# for i in range(1, M):
#     next = order[i]
#     if now <= next:
#         start, end = now, next
#     else:
#         start, end = next, now
#     visited[start:end] = list(map(plus_one, visited[start:end]))
#     now = next
# total_cost = 0
# for i in range(1, N):
#     cnt = visited[i]
#     if cnt:
#         ticket, card = cnt * info[i][0], cnt * info[i][1] + info[i][2]
#         total_cost += min(ticket, card)
# print(total_cost)


# 틀림
import sys
from math import ceil
new_input = sys.stdin.readline
N, M = map(int, new_input().split())
order = list(map(int, new_input().split()))
info = [0]
# info.extend([list(map(int, new_input().split())) for _ in range(N-1)])
limit = [0] * N
for i in range(N-1):
    info.append(list(map(int, new_input().split())))
    ticket_fee, card_fee, ic_card = info[-1]
    limit[i] = ceil(ic_card/(ticket_fee-card_fee))
visited = [0] * N
now = order[0]
def plus_one(number):
    return number+1
for i in range(1, M):
    next = order[i]
    if now <= next:
        start, end = now, next
    else:
        start, end = next, now
    visited[start:end] = list(map(plus_one, visited[start:end]))
    now = next
total_cost = 0
for i in range(1, N):
    cnt = visited[i]
    ticket, card = cnt * info[i][0], cnt * info[i][1] + info[i][2]
    total_cost += card if cnt >= limit[i] else ticket
print(total_cost)