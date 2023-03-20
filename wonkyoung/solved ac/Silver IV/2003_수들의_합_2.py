#230320
# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# start = end = cnt = 0
# total = nums[end]
# while start < N:
#     if total < M:
#         end += 1
#         if end < N:
#             total += nums[end]
#         else:
#             break
#     else:
#         if total == M:
#             cnt += 1
#         total -= nums[start]
#         start += 1
# print(cnt)


#
# def find_sum():
#     start = end = cnt = 0
#     total = nums[end]
#     while start < N:
#         if total < M:
#             end += 1
#             if end < N:
#                 total += nums[end]
#             else:
#                 break
#         else:
#             if total == M:
#                 cnt += 1
#             total -= nums[start]
#             start += 1
#     return cnt
#
# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# print(find_sum())

#
def find_sum():
    start = end = cnt = 0
    total = nums[end]
    while start < N:
        if total < M:
            end += 1
            if end >= N:
                break
            total += nums[end]
        elif total > M:
            total -= nums[start]
            start += 1
        else:
            cnt += 1
            total -= nums[start]
            start += 1
    return cnt

N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(find_sum())