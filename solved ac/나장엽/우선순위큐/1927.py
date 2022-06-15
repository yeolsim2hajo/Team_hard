import sys
input = sys.stdin.readline
import heapq

N = int(input())
que = []

for _ in range(N):
    number = int(input())
    if number == 0:
        if que:
            print(heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, number)

# 시간초과
# import sys
# input = sys.stdin.readline

# N = int(input())
# que = []

# for _ in range(N):
#     number = int(input())
#     if number == 0:
#         if len(que) == 0:
#             print(0)
#         else:
#             min_idx = que.index(min(que))
#             print(que.pop(min_idx))
#     else:
#         que.append(number)