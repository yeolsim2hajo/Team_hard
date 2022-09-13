#14575 뒤풀이
# import sys
# new_input = sys.stdin.readline
# N, T = map(int, new_input().split())
# min_limit, max_limit = [], []
# min_total = max_total = 0
# for _ in range(N):
#     min_alcohol, max_alcohol = map(int, new_input().split())
#     min_limit.append(min_alcohol)
#     max_limit.append(max_alcohol)
#     min_total += min_alcohol
#     max_total += max_alcohol
#
# if min_total > T or max_total < T:
#     print(-1)
# elif min_total == T:
#     print(max(min_limit))
# elif max_total == T:
#     print(max(max_limit))
# else:
#     start, end = 0, T
#     S = -1
#     while start <= end:
#         mid = (start+end)//2
#         min_dif = max_dif = 0
#         dif, temp = mid * N - T, mid
#         for i in range(N):
#             max_value, min_value = max_limit[i], min_limit[i]
#             if max_value <= mid:
#                 min_dif += max_value - min_value
#                 dif -= mid - max_value
#             elif min_value > mid:
#                 temp = max(min_value, temp)
#                 max_dif += max_value - min_value
#                 dif -= mid - min_value
#             else:
#                 min_dif += mid - min_value
#                 max_dif += max_value - mid
#         else:
#             if dif >= 0:
#                 if min_dif >= dif:
#                     S = min(S, temp) if S != -1 else temp
#                 end = mid - 1
#             else:
#                 if max_dif >= -dif:
#                     S = min(S, temp) if S != -1 else temp
#                 start = mid + 1
#     print(S)


# 함수로 변환
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     N, T = map(int, new_input().split())
#     min_limit, max_limit = [], []
#     min_total = max_total = 0
#     for _ in range(N):
#         min_alcohol, max_alcohol = map(int, new_input().split())
#         min_limit.append(min_alcohol)
#         max_limit.append(max_alcohol)
#         min_total += min_alcohol
#         max_total += max_alcohol
#
#     if min_total > T or max_total < T:
#         return -1
#     elif min_total == T:
#         return max(min_limit)
#     elif max_total == T:
#         return max(max_limit)
#     else:
#         start, end = 0, T
#         S = -1
#         while start <= end:
#             mid = (start+end)//2
#             min_dif = max_dif = 0
#             dif, temp = mid * N - T, mid
#             for i in range(N):
#                 max_value, min_value = max_limit[i], min_limit[i]
#                 if max_value <= mid:
#                     min_dif += max_value - min_value
#                     dif -= mid - max_value
#                 elif min_value > mid:
#                     temp = max(min_value, temp)
#                     max_dif += max_value - min_value
#                     dif -= mid - min_value
#                 else:
#                     min_dif += mid - min_value
#                     max_dif += max_value - mid
#             else:
#                 if dif >= 0:
#                     if min_dif >= dif:
#                         S = min(S, temp) if S != -1 else temp
#                     end = mid - 1
#                 else:
#                     if max_dif >= -dif:
#                         S = min(S, temp) if S != -1 else temp
#                     start = mid + 1
#     return S
# print(find_answer())


# sum 사용
# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     N, T = map(int, new_input().split())
#     min_limit, max_limit = [], []
#     for _ in range(N):
#         min_alcohol, max_alcohol = map(int, new_input().split())
#         min_limit.append(min_alcohol)
#         max_limit.append(max_alcohol)
#
#     min_total = sum(min_limit)
#     max_total = sum(max_limit)
#
#     if min_total > T or max_total < T:
#         return -1
#     elif min_total == T:
#         return max(min_limit)
#     elif max_total == T:
#         return max(max_limit)
#     else:
#         start, end = 0, T
#         S = -1
#         while start <= end:
#             mid = (start + end) // 2
#             min_dif = max_dif = 0
#             dif, temp = mid * N - T, mid
#             for i in range(N):
#                 max_value, min_value = max_limit[i], min_limit[i]
#                 if max_value <= mid:
#                     min_dif += max_value - min_value
#                     dif -= mid - max_value
#                 elif min_value > mid:
#                     temp = max(min_value, temp)
#                     max_dif += max_value - min_value
#                     dif -= mid - min_value
#                 else:
#                     min_dif += mid - min_value
#                     max_dif += max_value - mid
#             else:
#                 if dif >= 0:
#                     if min_dif >= dif:
#                         S = min(S, temp) if S != -1 else temp
#                     end = mid - 1
#                 else:
#                     if max_dif >= -dif:
#                         S = min(S, temp) if S != -1 else temp
#                     start = mid + 1
#     return S
#
# print(find_answer())


# def find_answer():
#     import sys
#     new_input = sys.stdin.readline
#     N, T = map(int, new_input().split())
#     min_limit, max_limit = [], []
#     for _ in range(N):
#         min_alcohol, max_alcohol = map(int, new_input().split())
#         min_limit.append(min_alcohol)
#         max_limit.append(max_alcohol)
#
#     min_total = sum(min_limit)
#     max_total = sum(max_limit)
#
#     if min_total > T or max_total < T:
#         return -1
#     elif min_total == T:
#         return max(min_limit)
#     elif max_total == T:
#         return max(max_limit)
#     else:
#         start, end = T//N, T-N+1
#         S = -1
#         while start <= end:
#             mid = (start + end) // 2
#             min_dif = max_dif = 0
#             dif, temp = mid * N - T, mid
#             for i in range(N):
#                 max_value, min_value = max_limit[i], min_limit[i]
#                 if max_value <= mid:
#                     min_dif += max_value - min_value
#                     dif -= mid - max_value
#                 elif min_value > mid:
#                     temp = max(min_value, temp)
#                     max_dif += max_value - min_value
#                     dif -= mid - min_value
#                 else:
#                     min_dif += mid - min_value
#                     max_dif += max_value - mid
#             else:
#                 if dif >= 0:
#                     if min_dif >= dif:
#                         S = min(S, temp) if S != -1 else temp
#                     end = mid - 1
#                 else:
#                     if max_dif >= -dif:
#                         S = min(S, temp) if S != -1 else temp
#                     start = mid + 1
#     return S
#
# print(find_answer())