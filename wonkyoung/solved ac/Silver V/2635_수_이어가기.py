#230201
# 피보나치
# first = int(input())
# def find_number(first):
#     bottom, top = 1, 1
#     proper_num = [1]
#     while True:
#         # 작거나 같은 부분
#         end = (first * top) // bottom
#         bottom, top = bottom + top, bottom
#         # 크거나 같은 부분
#         start = (first * top - 1) // bottom + 1
#         if start > end:
#             return proper_num[0]
#         proper_num = list(range(start, end+1))
#         bottom, top = bottom + top, bottom
#
# now = find_number(first)
# num_list = [first, now]
# cnt = 1
# while now >= 0:
#     new_num = num_list[-2] - num_list[-1]
#     if new_num >= 0:
#         num_list.append(new_num)
#     cnt += 1
#     now = new_num
# print(cnt)
# print(*num_list)

# 정리
# def return_answer():
#     def find_number(first):
#         bottom, top = 1, 1
#         proper_num = [1]
#         while True:
#             end = (first * top) // bottom
#             bottom, top = bottom + top, bottom
#             start = (first * top - 1) // bottom + 1
#             if start > end:
#                 return proper_num
#             proper_num = start
#             bottom, top = bottom + top, bottom
#
#     def find_cnt():
#         cnt = 1
#         now = find_number(first)
#         num_list = [first, now]
#         while now >= 0:
#             new_num = num_list[-2] - num_list[-1]
#             if new_num >= 0:
#                 num_list.append(new_num)
#             cnt += 1
#             now = new_num
#         print(cnt)
#         return num_list
#
#     first = int(input())
#     print(*find_cnt())
# return_answer()

# new_num 없애기
# def return_answer():
#     def find_number(first):
#         bottom, top = 1, 1
#         proper_num = [1]
#         while True:
#             end = (first * top) // bottom
#             bottom, top = bottom + top, bottom
#             start = (first * top - 1) // bottom + 1
#             if start > end:
#                 return proper_num
#             proper_num = start
#             bottom, top = bottom + top, bottom
#
#     def find_cnt():
#         cnt = 1
#         now = find_number(first)
#         num_list = [first, now]
#         while now >= 0:
#             now = num_list[-2] - now
#             if now >= 0:
#                 num_list.append(now)
#             cnt += 1
#         print(cnt)
#         return num_list
#
#     first = int(input())
#     print(*find_cnt())
# return_answer()

# return
def return_answer():
    def find_number(first):
        bottom, top = 1, 1
        proper_num = [1]
        while True:
            end = (first * top) // bottom
            bottom, top = bottom + top, bottom
            start = (first * top - 1) // bottom + 1
            if start > end:
                return proper_num
            proper_num = start
            bottom, top = bottom + top, bottom

    def find_cnt():
        cnt = 1
        now = find_number(first)
        num_list = [first, now]
        while True:
            cnt += 1
            now = num_list[-2] - now
            if now < 0:
                print(cnt)
                return num_list
            num_list.append(now)

    first = int(input())
    print(*find_cnt())
return_answer()