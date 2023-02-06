# 221211
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


# heap 사용 - 틀림
# from heapq import heapify, heappop, heappush
# N = int(input())
# def minus_int(num):
#     return -int(num)
# amount = sorted(map(minus_int, input().split()))
# heapify(amount)
# if N == 1:
#     min_time = amount[0]
# else:
#     min_time = 0
#     while amount:
#         max_val = heappop(amount)
#         if not amount:
#             min_time -= max_val
#             break
#         second_max_val = heappop(amount)
#         min_time -= second_max_val
#         heappush(amount, max_val - second_max_val)
#         # print(amount, min_time)
# if min_time > 1440:
#     print(-1)
# else:
#     print(min_time)


#230131
N = int(input())
snow_list = sorted(map(int, input().split()), reverse=True)
if N == 1 and snow_list[0] > 1440:
    print(-1)
elif sum(snow_list) > 2880:
    print(-1)
else:
    min_time = 0
    length = N
    while min_time <= 1440:
        first, last = snow_list[0], snow_list[-1]
        while length > 1:
            # print(min_time, snow_list)
            if first and last:
                snow_list[0] -= 1
                snow_list[-1] -= 1
                min_time += 1
                break
            elif first:
                snow_list.pop()
                length -= 1
                last = snow_list[-1]
            else:
                snow_list.pop(0)
                length -= 1
                first = snow_list[0]
        else:
            min_time += snow_list[0]
            if min_time <= 1440:
                print(min_time)
            else:
                print(-1)
            break
    else:
        print(-1)



