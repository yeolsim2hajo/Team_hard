#230214
# 시간 초과 날 것 같음
# staff, balloon = map(int, input().split())
# period = sorted(map(lambda x: [int(x), 0], input().split()))
# cnt = min_time = 0
# while True:
#     min_time += 1
#     for i in range(staff):
#         fixed_time, passed_time = period[i]
#         if fixed_time == passed_time:
#             period[i][1] = 0
#             cnt += 1
#         else:
#             period[i][1] += 1
#     if cnt >= balloon:
#         break
# print(min_time)

# 49 틀림
# staff, balloon = map(int, input().split())
# period = list(map(int, input().split()))
# start, end = 1, int(1e6)
# while start <= end:
#     mid = (start + end) // 2
#     cnt = sum(mid//period[i] for i in range(staff))
#     if cnt >= balloon:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(start)

# 1 틀림
# staff, balloon = map(int, input().split())
# period = list(map(int, input().split()))
# start, end = 1, int(1e6)
# while start <= end:
#     mid = (start + end) // 2
#     cnt = sum(mid//period[i] for i in range(staff))
#     if cnt >= balloon:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(mid)

# start
# staff, balloon = map(int, input().split())
# period = list(map(int, input().split()))
# start, end = 1, int(1e6) * max(period)
# while start <= end:
#     mid = (start + end) // 2
#     cnt = sum(mid//period[i] for i in range(staff))
#     if cnt >= balloon:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(start)


# end 범위 줄임
# staff, balloon = map(int, input().split())
# period = list(map(int, input().split()))
# start, end = 1, balloon * max(period)
# while start <= end:
#     mid = (start + end) // 2
#     cnt = sum(mid//period[i] for i in range(staff))
#     if cnt >= balloon:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(start)


# 모듈화
# def return_min_time():
#     staff, balloon = map(int, input().split())
#     period = list(map(int, input().split()))
#     start, end = 1, balloon * max(period)
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = sum(mid//period[i] for i in range(staff))
#         if cnt >= balloon:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start
# print(return_min_time())

# map 사용 - 더 걸림
# def return_min_time():
#     staff, balloon = map(int, input().split())
#     period = list(map(int, input().split()))
#     start, end = 1, balloon * max(period)
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = sum(map(lambda x: mid//x, period))
#         if cnt >= balloon:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start
# print(return_min_time())

#
# def return_min_time():
#     staff, balloon = map(int, input().split())
#     period = list(map(int, input().split()))
#     start, end = 1, balloon * max(period)
#
#     while start <= end:
#         mid = (start + end) // 2
#         find_quot = lambda x: mid // x
#         cnt = sum(map(find_quot, period))
#         if cnt >= balloon:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start
# print(return_min_time())

# 이분탐색 두 번
# def return_min_time():
#     staff, balloon = map(int, input().split())
#     period = sorted(map(int, input().split()))
#     start, end = balloon * period[0] // staff, balloon * period[-1]
#
#     def find_start_index(top, bottom_list):
#         if top > bottom_list[0]:
#             return 0
#         if top < bottom_list[-1]:
#             return staff
#         start, end = 0, staff-1
#         while start <= end:
#             mid = (start + end) // 2
#             bottom = bottom_list[mid]
#             if bottom > top:
#                 end = mid - 1
#             elif bottom < top:
#                 start = mid + 1
#             else:
#                 return mid
#         return start
#
#     while start <= end:
#         mid = (start + end) // 2
#         start_i = find_start_index(mid, period)
#         cnt = sum(mid//period[i] for i in range(start_i, staff))
#         if cnt >= balloon:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start
# print(return_min_time())

#
# def return_min_time():
#     staff, balloon = map(int, input().split())
#     period = list(map(int, input().split()))
#     start, end = 1, balloon * max(period)
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = sum(mid//bottom for bottom in period)
#         if cnt >= balloon:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start
# print(return_min_time())

#
# def return_min_time():
#     staff, balloon = map(int, input().split())
#     period = list(map(int, input().split()))
#     start, end = 1, balloon * max(period)
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = 0
#         for bottom in period:
#             cnt += mid//bottom
#         if cnt >= balloon:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return start
# print(return_min_time())

#
def return_min_time():
    staff, balloon = map(int, input().split())
    period = list(map(int, input().split()))
    start, end = 1, balloon * max(period)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for bottom in period:
            cnt += mid//bottom
        if cnt >= balloon:
            end = mid - 1
        else:
            start = mid + 1
    return start
print(return_min_time())