#220111
# deque
# from collections import deque
# N = int(input())
# worms, cnt = deque(), 1
# worms.append((1, 3))
# for year in range(2, N+1):
#     i, new_worms = 0, deque()
#     new_limit = 3 if year%2 else 4
#     while i < cnt:
#         now, limit = worms[i]
#         if now < limit:
#             new_worms.append((now+1, limit))
#         new_worms.append((1, new_limit))
#         i += 1
#     cnt = len(new_worms)
#     worms = [new_worms[j][:] for j in range(cnt)]
# print(cnt)



# list
# N = int(input())
# worms, cnt = [], 1
# worms.append((1, 3))
# for year in range(2, N+1):
#     i, new_worms = 0, []
#     new_limit = 3 if year%2 else 4
#     while i < cnt:
#         now, limit = worms[i]
#         if now < limit:
#             new_worms.append((now+1, limit))
#         new_worms.append((1, new_limit))
#         i += 1
#     cnt = len(new_worms)
#     worms = [new_worms[j][:] for j in range(cnt)]
# print(cnt)


# 함수형
# def find_cnt(N):
#     worms, cnt = [(1, 3)], 1
#     for year in range(2, N + 1):
#         i, new_worms = 0, []
#         new_limit = 3 if year % 2 else 4
#         while i < cnt:
#             now, limit = worms[i]
#             if now < limit:
#                 new_worms.append((now + 1, limit))
#             new_worms.append((1, new_limit))
#             i += 1
#         cnt = len(new_worms)
#         worms = [new_worms[j][:] for j in range(cnt)]
#     return cnt
#
# N = int(input())
# print(find_cnt(N))