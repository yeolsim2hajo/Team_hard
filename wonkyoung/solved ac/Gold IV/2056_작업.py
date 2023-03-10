#230310
# from sys import stdin
# from heapq import heappush, heappop
# new_input = stdin.readline
# N = int(new_input())
# next_work = [[] for _ in range(N+1)]
# finished = [False] * (N+1)
# q = []
# for i in range(1, N+1):
#     work_time, cnt, *works = map(int, new_input().split())
#     if cnt == 0:
#         heappush(q, (work_time, i))
#     else:
#         for j in works:
#             next_work[j].append((i, work_time, cnt, works))
# min_work = 0
# while q:
#     finish_time, num = heappop(q)
#     if not finished[num]:
#         finished[num] = True
#         for next_num in next_work[num]:
#             for i in next_num[3]:
#                 if not finished[i]:
#                     break
#             else:
#                 heappush(q, (finish_time+next_num[1], next_num[0]))
#         if finish_time > min_work:
#             min_work = finish_time
# print(min_work)


#
# def find_min_work():
#     from sys import stdin
#     from heapq import heappush, heappop
#     new_input = stdin.readline
#     N = int(new_input())
#     next_work = [[] for _ in range(N+1)]
#     finished = [False] * (N+1)
#     q = []
#     def fill_arr():
#         for i in range(1, N+1):
#             work_time, cnt, *works = map(int, new_input().split())
#             if cnt == 0:
#                 heappush(q, (work_time, i))
#             else:
#                 for j in works:
#                     next_work[j].append((i, work_time, cnt, works))
#         def calc_time():
#             min_work = 0
#             while q:
#                 finish_time, num = heappop(q)
#                 if not finished[num]:
#                     finished[num] = True
#                     for next_num in next_work[num]:
#                         for i in next_num[3]:
#                             if not finished[i]:
#                                 break
#                         else:
#                             heappush(q, (finish_time+next_num[1], next_num[0]))
#                     if finish_time > min_work:
#                         min_work = finish_time
#             return min_work
#         return calc_time()
#     return fill_arr()
# print(find_min_work())



#
def find_min_work():
    from sys import stdin
    from heapq import heappush, heappop
    new_input = stdin.readline
    N = int(new_input())
    next_work = [[] for _ in range(N+1)]
    work_info = [[] for _ in range(N+1)]
    finished = [False] * (N+1)
    q = []
    def fill_arr():
        for work_num in range(1, N+1):
            work_time, cnt, *works = map(int, new_input().split())
            if cnt == 0:
                heappush(q, (work_time, work_num))
            else:
                work_info[work_num].extend([work_time, cnt, works])
                for pre_work in works:
                    next_work[pre_work].append(work_num)
        def calc_time():
            min_work = 0
            while q:
                finish_time, num = heappop(q)
                if not finished[num]:
                    finished[num] = True
                    pre_num_list = next_work[num]
                    for pre_num in pre_num_list:
                        for i in work_info[pre_num][2]:
                            if not finished[i]:
                                break
                        else:
                            heappush(q, (finish_time+work_info[pre_num][0], pre_num))
                    if finish_time > min_work:
                        min_work = finish_time
            return min_work
        return calc_time()
    return fill_arr()
print(find_min_work())
