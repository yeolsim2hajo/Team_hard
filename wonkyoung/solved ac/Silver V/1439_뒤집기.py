#230122
# binary_str = input()
# length = len(binary_str)
# min_cnt = length
# for num in ('0', '1'):
#     cnt = 0
#     start = end = -1
#     for i in range(length):
#         if binary_str[i] == num:
#             if start == -1:
#                 start = i
#         elif start != -1:
#             cnt += 1
#             start = -1
#     if start != -1:
#         cnt += 1
#     if min_cnt > cnt:
#         min_cnt = cnt
# print(min_cnt)

# 정리
# def find_cnt():
#     length = len(binary_str)
#     min_cnt = length
#     for num in ('0', '1'):
#         cnt, start = 0, -1
#         for i in range(length):
#             if binary_str[i] == num:
#                 if start == -1:
#                     start = i
#             elif start != -1:
#                 cnt += 1
#                 start = -1
#         if start != -1:
#             cnt += 1
#         if min_cnt > cnt:
#             min_cnt = cnt
#     return min_cnt
# binary_str = input()
# print(find_cnt())


def find_cnt(binary_str):
    length = len(binary_str)
    min_cnt = length
    for num in ('0', '1'):
        cnt, start = 0, -1
        for i in range(length):
            if binary_str[i] == num:
                if start == -1:
                    start = i
            elif start != -1:
                cnt += 1
                start = -1
        if start != -1:
            cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
    return min_cnt
binary_str = input()
print(find_cnt(binary_str))
