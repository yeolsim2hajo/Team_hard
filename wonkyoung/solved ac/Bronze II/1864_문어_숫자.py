#221209
# import sys
#
# patterns = {'-': 0, '\\': 1, '(': 2,
#             '@': 3, '?': 4, '>': 5,
#             '&': 6, '%': 7, '/': -1}
# new_input = sys.stdin.readline
# while True:
#     octo_num = new_input().rstrip()
#     if octo_num == '#':
#         break
#     length = len(octo_num)
#     match_num = 0
#     for i in range(length):
#         match_num += patterns[octo_num[i]]  * 8 ** (length - i - 1)
#     print(match_num)


# 함수로
# def conv_num():
#     import sys
#     new_input = sys.stdin.readline
#     patterns = {'-': 0, '\\': 1, '(': 2,
#                 '@': 3, '?': 4, '>': 5,
#                 '&': 6, '%': 7, '/': -1}
#     while True:
#         octo_num = new_input().rstrip()
#         if octo_num == '#':
#             return
#         length = len(octo_num)
#         match_num = 0
#         for i in range(length):
#             match_num += patterns[octo_num[i]]  * 8 ** (length - i - 1)
#         print(match_num)
# conv_num()



# 좀 더 정리
def conv_num():
    import sys
    new_input = sys.stdin.readline
    patterns = {'-': 0, '\\': 1, '(': 2,
                '@': 3, '?': 4, '>': 5,
                '&': 6, '%': 7, '/': -1}
    while True:
        octo_num = new_input().rstrip()
        if octo_num == '#':
            return
        length, match_num = len(octo_num), 0

        for i in range(length):
            pattern, multiple_num = patterns[octo_num[i]], 8 ** (length - i - 1)
            match_num += pattern * multiple_num
        print(match_num)

conv_num()