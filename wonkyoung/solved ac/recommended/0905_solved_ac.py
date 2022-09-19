#14575 뒤풀이
# import sys
#
# new_input = sys.stdin.readline
# N, T = map(int, new_input().split())
# S = 0
# alcohol_min, alcohol_max = [], []
# total_min = 0
# for _ in range(N):
#     min_limit, max_limit = map(int, new_input().split())
#     alcohol_min.append(min_limit)
#     alcohol_max.append(max_limit)
#     total_min += min_limit
# if total_min > T:
#     S = -1
# elif total_min < T:
#     total_max = sum(alcohol_max)
#     if total_max < T:
#         S = -1
#     elif total_max > T:
#         start, end = 0, T
#         S = pre_S = 0
#         while start <= end:
#             average = (start + end)//N
#             mid = (start + end)//2
#             total = average*N
#             for i in range(N):
#                 if alcohol_min[i] > average:
#                     dif_min = alcohol_min[i] - average
#                     total += dif_min
#                     S = alcohol_min[i]
#                 elif alcohol_max[i] < average:
#                     dif_max = average - alcohol_max[i]
#                     total -= dif_max
#             if total < T:
#                 start = mid + 1
#             elif total > T:
#                 end = mid - 1
#             else:
#                 pre_S = min(S, pre_S)
#                 start = average + 1
#         S = pre_S
#     else:
#         S = max(alcohol_max)
# else:
#     S = max(alcohol_min)
# print(S)


#1173 운동
# N, m, M, T, R = map(int, input().split())
# plus = N * T
# if plus + m <= M:
#     answer = N
# elif m + T > M:
#     answer = -1
# else:
#     answer = practice = 0
#     now = m
#     while practice < N:
#         if now + T <= M:
#             practice += 1
#             now += T
#         elif now - R >= m:
#             now -= R
#         else:
#             now = m
#         answer += 1
# print(answer)


# plus 없앰
# N, m, M, T, R = map(int, input().split())
# if N * T + m <= M:
#     answer = N
# elif m + T > M:
#     answer = -1
# else:
#     answer = practice = 0
#     now = m
#     while practice < N:
#         if now + T <= M:
#             practice += 1
#             now += T
#         elif now - R >= m:
#             now -= R
#         else:
#             now = m
#         answer += 1
# print(answer)

# True & break
# N, m, M, T, R = map(int, input().split())
# if N * T + m <= M:
#     answer = N
# elif m + T > M:
#     answer = -1
# else:
#     answer = practice = 0
#     now = m
#     while True:
#         if now + T <= M:
#             practice += 1
#             if practice == N:
#                 answer += 1
#                 break
#             now += T
#         elif now - R >= m:
#             now -= R
#         else:
#             now = m
#         answer += 1
# print(answer)


# 함수형으로 변환 - 시간 더 걸림
# def find_answer():
#     N, m, M, T, R = map(int, input().split())
#     if N * T + m <= M:
#         answer = N
#     elif m + T > M:
#         answer = -1
#     else:
#         answer = practice = 0
#         now = m
#         while True:
#             if now + T <= M:
#                 practice += 1
#                 if practice == N:
#                     answer += 1
#                     return answer
#                 now += T
#             elif now - R >= m:
#                 now -= R
#             else:
#                 now = m
#             answer += 1
#     return answer
# print(find_answer())
