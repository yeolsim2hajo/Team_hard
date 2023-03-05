#230302
# 틀림
# def find_dif():
#     from sys import stdin
#     new_input = stdin.readline
#     N, C = map(int, new_input().split())
#     houses = sorted(int(new_input()) for _ in range(N))
#     max_dif = (houses[-1] - houses[0])//(C-1)
#     if C == 2:
#         return max_dif
#     if C == N:
#         for i in range(N-1):
#             dif = houses[i+1] - houses[i]
#             if dif < max_dif:
#                 max_dif = dif
#                 if max_dif == 1:
#                     return 1
#         return max_dif
#
#     def search_dif():
#         # 개수 찾기
#         def calc_cnt():
#             cnt = 1
#             start, end = 0, N - 1
#             target = houses[0] + dif
#             for _ in range(C-1):
#                 while start <= end:
#                     mid = (start + end)//2
#                     house = houses[mid]
#                     if house > target:
#                         end = mid - 1
#                     elif house < target:
#                         start = mid + 1
#                     else:
#                         start = mid + 1
#                         target += dif
#                         break
#                 if start >= N:
#                     break
#                 target = houses[end] + dif
#                 cnt += 1
#                 end = N - 1
#             return cnt
#         # 거리 찾기
#         start_dif, end_dif = 1, max_dif
#         while start_dif <= end_dif:
#             dif = (start_dif + end_dif)//2
#             cnt = calc_cnt()
#             if cnt < C:
#                 end_dif = dif - 1
#             else:
#                 start_dif = dif + 1
#         if start_dif > max_dif:
#             return max_dif
#         return start_dif
#
#     return search_dif()
# print(find_dif())
'''
5 3
1
2
8
4
9
'''
'''
5 4
1
3
8
4
12
'''
'''
5 4
1
3
8
4
10
'''

# 230305
# def find_max_dif():
#     from sys import stdin
#     new_input = stdin.readline
#     N, C = map(int, new_input().split())
#     houses = [int(new_input()) for _ in range(N)]
#     houses.sort()
#
#     if N == 2:
#         return houses[-1] - houses[0]
#
#     def binary_search():
#         def binary_search2():
#             nonlocal cnt, max_dif
#             target = min_val + dif
#             start, end = 0, N - 1
#             while start <= end:
#                 while start <= end:
#                     mid = (start + end) // 2
#                     house = houses[mid]
#                     if target > house:
#                         start = mid + 1
#                     elif target < house:
#                         end = mid - 1
#                     else:
#                         start, end = mid+1, N-1
#                         cnt += 1
#                         target += dif
#                         break
#                 else:
#                     if start < N and houses[start] >= target:
#                         cnt += 1
#                         end = N - 1
#                         target = houses[start] + dif
#                     else:
#                         return
#                 if cnt >= C - 1:
#                     if max_dif < dif:
#                         max_dif = dif
#                     return
#         max_val, min_val = houses[-1], houses[0]
#         start_dif, end_dif = 1, (max_val - min_val)//(C-1)
#         max_dif = 1
#         while start_dif <= end_dif:
#             dif = (start_dif + end_dif)//2
#             cnt = 0
#             binary_search2()
#             if cnt >= C - 1:
#                 start_dif = dif + 1
#             else:
#                 end_dif = dif - 1
#         return max_dif
#
#     return binary_search()
# print(find_max_dif())



#
# def find_max_dif():
#     from sys import stdin
#     new_input = stdin.readline
#     N, C = map(int, new_input().split())
#     houses = [int(new_input()) for _ in range(N)]
#     houses.sort()
#
#     if N == 2:
#         return houses[-1] - houses[0]
#
#     def binary_search():
#         def binary_search2(target):
#             nonlocal cnt
#             start, end = 0, N - 1
#             while start <= end:
#                 while start <= end:
#                     mid = (start + end) // 2
#                     house = houses[mid]
#                     if target > house:
#                         start = mid + 1
#                     elif target < house:
#                         end = mid - 1
#                     else:
#                         start, end = mid+1, N-1
#                         cnt += 1
#                         target += dif
#                         break
#                 else:
#                     if start < N and houses[start] >= target:
#                         cnt += 1
#                         end = N - 1
#                         target = houses[start] + dif
#                     else:
#                         return
#         max_val, min_val = houses[-1], houses[0]
#         start_dif, end_dif = 1, (max_val - min_val)//(C-1)
#         max_dif = 1
#         while start_dif <= end_dif:
#             dif = (start_dif + end_dif)//2
#             cnt = 0
#             binary_search2(min_val + dif)
#             if cnt >= C - 1:
#                 start_dif = dif + 1
#                 if max_dif < dif:
#                     max_dif = dif
#             else:
#                 end_dif = dif - 1
#         return max_dif
#
#     return binary_search()
#
# print(find_max_dif())


#
def find_max_dif():
    from sys import stdin
    new_input = stdin.readline
    N, C = map(int, new_input().split())
    houses = [int(new_input()) for _ in range(N)]
    houses.sort()

    if N == 2:
        return houses[-1] - houses[0]

    def binary_search2(target):
        nonlocal cnt
        start, end = 0, N - 1
        while start <= end:
            while start <= end:
                mid = (start + end) // 2
                house = houses[mid]
                if target > house:
                    start = mid + 1
                elif target < house:
                    end = mid - 1
                else:
                    start, end = mid+1, N-1
                    cnt += 1
                    target += dif
                    break
            else:
                if start < N and houses[start] >= target:
                    cnt += 1
                    end = N - 1
                    target = houses[start] + dif
                else:
                    return
    max_val, min_val = houses[-1], houses[0]
    start_dif, end_dif = 1, (max_val - min_val)//(C-1)
    max_dif = 1
    while start_dif <= end_dif:
        dif = (start_dif + end_dif)//2
        cnt = 0
        binary_search2(min_val + dif)
        if cnt >= C - 1:
            start_dif = dif + 1
            if max_dif < dif:
                max_dif = dif
        else:
            end_dif = dif - 1
    return max_dif

print(find_max_dif())