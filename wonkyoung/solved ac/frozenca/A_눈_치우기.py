# 틀림
# N = int(input())
# amount = sorted(map(int, input().split()))
# if N == 1:
#     min_time = amount[0]
# else:
#     start, end = 0, N-1
#     min_time = 0
#     while start <= end:
#         start_val, end_val = amount[start], amount[end]
#         if end_val >= start_val:
#             amount[end] -= start_val
#             amount[start] = 0
#             min_time += start_val
#             start += 1
#         else:
#             amount[start] -= end_val
#             amount[end] = 0
#             min_time += end_val
#             end -= 1
#         print(amount, min_time)
# if min_time > 1440:
#     print(-1)
# else:
#     print(min_time)


# 뒤에서부터 (덜 틀림)
# N = int(input())
# amount = sorted(map(int, input().split()))
# if N == 1:
#     min_time = amount[0]
# else:
#     start, end = N-2, N-1
#     min_time = 0
#     while start >= 0:
#         start_val, end_val = amount[start], amount[end]
#         if end_val >= start_val:
#             amount[end] -= start_val
#             amount[start] = 0
#             min_time += start_val
#             start -= 1
#         else:
#             amount[start] -= end_val
#             amount[end] = 0
#             min_time += end_val
#             start -= 1
#             end = start + 1
#         # print(amount, min_time)
#     if amount[end]:
#         min_time += amount[end]
# if min_time > 1440:
#     print(-1)
# else:
#     print(min_time)

# 7
# 12 543 45 32 3 80 2

# 7
# 12 43 9 23 38 21 32


# heap 사용
from heapq import heapify, heappop, heappush
N = int(input())
def minus_int(num):
    return -int(num)
amount = sorted(map(minus_int, input().split()))
heapify(amount)
if N == 1:
    min_time = amount[0]
else:
    min_time = 0
    while amount:
        max_val = heappop(amount)
        if not amount:
            min_time -= max_val
            break
        second_max_val = heappop(amount)
        min_time -= second_max_val
        heappush(amount, max_val - second_max_val)
        # print(amount, min_time)
if min_time > 1440:
    print(-1)
else:
    print(min_time)

