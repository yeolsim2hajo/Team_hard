#230218
# def min_jealousy():
#     from sys import stdin
#     new_input = stdin.readline
#     child, colors = map(int, new_input().split())
#     final_colors, total = colors, 0
#     cnt_list = []
#     def fill_var():
#         nonlocal final_colors, child, total
#         for _ in range(colors):
#             jewel = int(new_input())
#             if jewel == 1:
#                 final_colors -= 1
#                 child -= 1
#             else:
#                 cnt_list.append(jewel)
#                 total += jewel
#     def find_jealousy():
#         start, end = 1, max(cnt_list)
#         while start <= end:
#             mid = (start + end) // 2
#             min_child = 0
#             for cnt in cnt_list:
#                 min_child += cnt // mid
#                 if cnt % mid:
#                     min_child += 1
#             if min_child > child:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return start
#
#     fill_var()
#     if not cnt_list: return 1
#     elif total <= child: return 1
#     elif child == 1: return cnt_list[0]
#     return find_jealousy()
#
# print(min_jealousy())



#
# def min_jealousy():
#     from sys import stdin
#     new_input = stdin.readline
#     child, colors = map(int, new_input().split())
#     final_colors, total = colors, 0
#     cnt_list = []
#     def fill_var():
#         nonlocal final_colors, child, total
#         for _ in range(colors):
#             jewel = int(new_input())
#             if jewel == 1:
#                 final_colors -= 1
#                 child -= 1
#             else:
#                 cnt_list.append(jewel)
#                 total += jewel
#     def find_jealousy():
#         start, end = 1, max(cnt_list)
#         while start <= end:
#             mid = (start + end) // 2
#             min_child = 0
#             for cnt in cnt_list:
#                 min_child += cnt // mid + int(cnt % mid > 0)
#             if min_child > child:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return start
#
#     fill_var()
#     if not cnt_list: return 1
#     elif total <= child: return 1
#     elif child == 1: return cnt_list[0]
#     return find_jealousy()
#
# print(min_jealousy())


#
# def min_jealousy():
#     from sys import stdin
#     new_input = stdin.readline
#     child, colors = map(int, new_input().split())
#     final_colors, total, max_cnt = colors, 0, 0
#     cnt_list = []
#     def fill_var():
#         nonlocal final_colors, child, total, max_cnt
#         for _ in range(colors):
#             jewel = int(new_input())
#             if jewel == 1:
#                 final_colors -= 1
#                 child -= 1
#             else:
#                 cnt_list.append(jewel)
#                 total += jewel
#                 if jewel > max_cnt:
#                     max_cnt = jewel
#     def find_jealousy():
#         start, end = 1, max_cnt
#         while start <= end:
#             mid = (start + end) // 2
#             min_child = 0
#             for cnt in cnt_list:
#                 min_child += cnt // mid
#                 if cnt % mid:
#                     min_child += 1
#             if min_child > child:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return start
#
#     fill_var()
#     if not cnt_list: return 1
#     elif total <= child: return 1
#     elif child == 1: return cnt_list[0]
#     return find_jealousy()
#
# print(min_jealousy())

#
def min_jealousy():
    from sys import stdin
    new_input = stdin.readline
    child, colors = map(int, new_input().split())
    final_colors, total, max_cnt = colors, 0, 0
    cnt_list = []
    def fill_var():
        nonlocal final_colors, child, total, max_cnt
        for _ in range(colors):
            jewel = int(new_input())
            if jewel == 1:
                final_colors -= 1
                child -= 1
            else:
                cnt_list.append(jewel)
                total += jewel
                if jewel > max_cnt:
                    max_cnt = jewel
    def find_jealousy():
        def calc_min(cnt):
            answer = cnt // mid
            if cnt % mid:
                return answer + 1
            return answer

        start, end = 1, max_cnt
        while start <= end:
            mid = (start + end) // 2
            min_child = sum(map(calc_min, cnt_list))
            if min_child > child:
                start = mid + 1
            else:
                end = mid - 1
        return start

    fill_var()
    if not cnt_list: return 1
    elif total <= child: return 1
    elif child == 1: return cnt_list[0]
    return find_jealousy()

print(min_jealousy())


