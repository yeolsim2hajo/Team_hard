#230118
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_total = -1000
#     for start in range(N):
#         total = 0
#         for end in range(start, N):
#             total += arr[end]
#             if total > max_total:
#                 max_total = total
#     print(max_total)


# 틀림
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_total, min_total = -1000, 1000
#     # max_i = -1
#     acc_arr = arr[:]
#     minus = [False] * N
#     if arr[0] < 0:
#         minus[0] = True
#     for i in range(1, N):
#         acc_arr[i] += acc_arr[i-1]
#         total = acc_arr[i]
#         if max_total < total:
#             max_total = total
#             max_i = i
#         if min_total > total:
#             min_total = total
#             min_i = i
#         if total < 0:
#             minus[i] = True
#
#     max_val = acc_arr[max_i]
#     for i in range(max_i-1, -1, -1):
#         minus_val = 0
#         if minus[i] and acc_arr[]:
#             minus_val
#     for i in range(N-1, 1):
#         total = acc_arr[i]
#         for j in range(i):
#             if minus[j]:
#                 temp_total = total - acc_arr[j]
#                 if temp_total > max_total:
#                     max_total = temp_total
#     # print(acc_arr)
#     print(max_total)