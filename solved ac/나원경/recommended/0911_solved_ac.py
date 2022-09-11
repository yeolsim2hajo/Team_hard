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
#     start, end = T//N, T-N+1
#     S = -1
#     while start <= end:
#         mid = (start+end)//2
#         min_dif = max_dif = 0
#         total, temp = mid * N, mid
#         for i in range(N):
#             max_value, min_value = max_limit[i], min_limit[i]
#             if max_value <= mid:
#                 min_dif += max_value - min_value
#                 total -= mid - max_value
#             elif min_value > mid:
#                 temp = min_value
#                 max_dif += max_value
#             else:
#                 min_dif += mid - min_value
#                 max_dif += max_value - mid
#         else:
#             if total >= T:
#                 if min_dif >= total - T:
#                     print(min_dif, total - T)
#                     S = min(S, mid) if S != -1 else mid
#                     print('two',S, start, end, mid)
#                 end = mid - 1
#             else:
#                 start = mid + 1
#     print(start, end)
#     dif = 0
#     for i in range(N):
#         if max_limit[i] <= start:
#             dif += max_limit[i] - min_limit[i]
#         elif min_limit[i] > start:
#             break
#         else:
#             dif += start - min_limit[i]
#     else:
#         if dif >= start * N - T:
#             S = min(S, start) if S != -1 else start
#     print(S)


#20053 최소, 최대 2
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     numbers = sorted(map(int, input().split()))
#     print(numbers[0], numbers[-1])


# for문 - 시간 덜 나옴
T = int(input())
for _ in range(T):
    N = int(input())
    max_val, min_val = int(-1e6), int(1e6)
    numbers = list(map(int, input().split()))
    for number in numbers:
        if max_val < number:
            max_val = number
        if min_val > number:
            min_val = number
    print(min_val, max_val)

# 함수 사용 - 가장 시간 덜 나옴
T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_val, min_val = max(numbers), min(numbers)
    print(min_val, max_val)











