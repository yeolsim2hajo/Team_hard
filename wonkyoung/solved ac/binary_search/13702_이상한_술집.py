#221112
# import sys
#
# new_input = sys.stdin.readline
# N, K = map(int, new_input().split())
# total = 0
# bucket= []
# for _ in range(N):
#     volume = int(new_input())
#     total += volume
#     bucket.append(volume)
# bucket.sort()
# max_volume = total//K
# start, end = 0, max_volume
# while start <= end:
#     mid = (start + end)//2
#     cnt = 0
#     start_index, end_index, initial_index = 0, N-1, -1
#     while start_index <= end_index:
#         mid_index = (start_index + end_index) //2
#         if bucket[mid_index] > mid:
#             end_index = mid_index - 1
#         elif bucket[mid_index] < mid:
#             start_index = mid_index + 1
#         else:
#             initial_index = mid_index
#             break
#     if initial_index == -1:
#         initial_index = end_index
#     for i in range(initial_index, N):
#         cnt += bucket[i]//mid
#     if cnt >= K:
#         start = mid + 1
#     else:
#         end = mid - 1
# if end < 0:
#     end = 0
# print(end)



# 이분탐색 한 번만
# import sys
#
# new_input = sys.stdin.readline
# N, K = map(int, new_input().split())
# total = 0
# bucket= []
# for _ in range(N):
#     volume = int(new_input())
#     total += volume
#     bucket.append(volume)
# bucket.sort()
# if total < K:
#     print(0)
# else:
#     max_volume = total//K
#     start, end = 0, max_volume
#     while start <= end:
#         mid = (start + end)//2
#         if mid == 0:
#             break
#         cnt = 0
#         for i in range(N):
#             cnt += bucket[i]//mid
#         if cnt >= K:
#             start = mid + 1
#         else:
#             end = mid - 1
#     print(end)


# 함수화
# def find_volume():
#     import sys
#     new_input = sys.stdin.readline
#     N, K = map(int, new_input().split())
#     total = 0
#     bucket= []
#     for _ in range(N):
#         volume = int(new_input())
#         total += volume
#         bucket.append(volume)
#     bucket.sort()
#     def binary_search():
#         if total < K:
#             return 0
#         max_volume = total//K
#         start, end = 0, max_volume
#         while start <= end:
#             mid = (start + end)//2
#             if mid == 0:
#                 return end
#             cnt = 0
#             for i in range(N):
#                 cnt += bucket[i]//mid
#             if cnt >= K:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return end
#     print(binary_search())
# find_volume()


# 두 개 적용 - 틀림
def find_volume():
    import sys
    new_input = sys.stdin.readline
    N, K = map(int, new_input().split())
    total = 0
    bucket= []
    for _ in range(N):
        volume = int(new_input())
        total += volume
        bucket.append(volume)
    bucket.sort()

    def another_search(mid):
        start_index, end_index = 0, N - 1
        while start_index <= end_index:
            mid_index = (start_index + end_index) // 2
            if bucket[mid_index] > mid:
                end_index = mid_index - 1
            elif bucket[mid_index] < mid:
                start_index = mid_index + 1
            else:
                return mid_index
        return end_index

    def binary_search():
        if total < K:
            return 0
        max_volume = total//K
        start, end = 0, max_volume
        while start <= end:
            mid = (start + end)//2
            if mid == 0:
                return end
            cnt = 0
            start_i = another_search(mid)
            for i in range(start_i, N):
                cnt += bucket[i]//mid
            if cnt >= K:
                start = mid + 1
            else:
                end = mid - 1
        return end
    print(binary_search())
find_volume()